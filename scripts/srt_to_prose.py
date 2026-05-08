# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Convert SRT subtitle files to readable prose.

Uses pause duration between subtitle blocks to infer:
- Sentence boundaries (medium pauses)
- Paragraph breaks (longer pauses)
- Section breaks (very long pauses)

Usage: uv run scripts/srt_to_prose.py <srt_file> [options]
       uv run scripts/srt_to_prose.py <srt_file> -o output.txt

Options:
  --thresholds=S,P,X   Set pause thresholds (sentence, paragraph, section)
  --skip-intro         Skip MIT OCW intro boilerplate (first ~20s)
  -o FILE              Write output to file instead of stdout
"""
import re
import sys
from pathlib import Path
from dataclasses import dataclass

# Thresholds in seconds (tuned based on gap distribution analysis)
# Gaps are bimodal: 92% are <0.3s, then jumps to 1.5s+ for intentional pauses
SENTENCE_PAUSE = 1.8      # pause suggesting end of sentence
PARAGRAPH_PAUSE = 3.5     # pause suggesting new paragraph
SECTION_PAUSE = 6.0       # pause suggesting new section/topic

# Skip intro up to this timestamp (MIT OCW boilerplate ends around here)
INTRO_END_MS = 22000

@dataclass
class Block:
    index: int
    start_ms: int
    end_ms: int
    text: str

def parse_timestamp(ts: str) -> int:
    """Parse SRT timestamp to milliseconds."""
    # Format: HH:MM:SS,mmm
    match = re.match(r'(\d+):(\d+):(\d+),(\d+)', ts.strip())
    if not match:
        raise ValueError(f"Invalid timestamp: {ts}")
    h, m, s, ms = map(int, match.groups())
    return ((h * 60 + m) * 60 + s) * 1000 + ms

def parse_srt(path: Path) -> list[Block]:
    """Parse SRT file into blocks."""
    content = path.read_text(encoding='utf-8')
    blocks = []

    # Split by blank lines (block separator)
    raw_blocks = re.split(r'\n\n+', content.strip())

    for raw in raw_blocks:
        lines = raw.strip().split('\n')
        if len(lines) < 3:
            continue

        # Line 1: index
        try:
            index = int(lines[0])
        except ValueError:
            continue

        # Line 2: timestamps
        ts_match = re.match(r'(.+?)\s*-->\s*(.+)', lines[1])
        if not ts_match:
            continue

        start_ms = parse_timestamp(ts_match.group(1))
        end_ms = parse_timestamp(ts_match.group(2))

        # Lines 3+: text
        text = ' '.join(lines[2:])
        text = re.sub(r'\s+', ' ', text).strip()

        blocks.append(Block(index, start_ms, end_ms, text))

    return blocks

def ends_with_sentence(text: str) -> bool:
    """Check if text ends with sentence-ending punctuation."""
    return bool(re.search(r'[.!?][\'"»"\']*$', text.strip()))

def is_incomplete(text: str) -> bool:
    """Check if text appears to be mid-sentence."""
    # Ends with comma, conjunction, preposition, article, etc.
    incomplete_endings = r'(,|and|or|but|the|a|an|to|of|for|in|on|at|by|with|that|which|who|is|are|was|were|have|has|had|will|would|could|should|can|may|might|must|this|these|those|if|when|where|how|what|why|as|so|than|then|also|just|even|only|very|more|most|such|some|any|all|each|every|both|either|neither|no|not|into|from|about|through|during|before|after|above|below|between|under|over|out|up|down|off|away|back|here|there|now|then|still|already|yet|again|always|never|often|sometimes|usually|probably|really|quite|rather|pretty|almost|nearly|about|around|exactly|simply|actually|certainly|definitely|perhaps|maybe|possibly|likely|sure|true|right|well|good|bad|new|old|big|small|long|short|high|low|few|many|much|little|own|other|another|same|different|next|last|first|second|third)$'
    return bool(re.search(incomplete_endings, text.strip().lower()))

def clean_text(text: str) -> str:
    """Clean up subtitle text artifacts."""
    # Remove speaker labels like "PROFESSOR:" at start
    text = re.sub(r'^[A-Z][A-Z\s]+:\s*', '', text)
    # Remove [inaudible], [music], etc.
    text = re.sub(r'\[.*?\]', '', text)
    # Clean up whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def convert_to_prose(blocks: list[Block],
                     sentence_pause: float = SENTENCE_PAUSE,
                     paragraph_pause: float = PARAGRAPH_PAUSE,
                     section_pause: float = SECTION_PAUSE,
                     skip_intro: bool = False) -> str:
    """Convert subtitle blocks to prose using pause-based heuristics."""

    if not blocks:
        return ""

    # Skip intro boilerplate if requested
    if skip_intro:
        blocks = [b for b in blocks if b.start_ms >= INTRO_END_MS]

    output = []
    current_paragraph = []

    for i, block in enumerate(blocks):
        text = clean_text(block.text)
        if not text:
            continue

        # Calculate gap from previous block
        if i > 0:
            gap_ms = block.start_ms - blocks[i-1].end_ms
            gap_s = gap_ms / 1000.0
        else:
            gap_s = 0

        # Determine how to join with previous text
        if i == 0:
            current_paragraph.append(text)
        elif gap_s >= section_pause:
            # Section break: flush paragraph, add separator
            if current_paragraph:
                output.append(' '.join(current_paragraph))
                current_paragraph = []
            output.append('\n---\n')
            current_paragraph.append(text)
        elif gap_s >= paragraph_pause:
            # Paragraph break: flush current paragraph
            if current_paragraph:
                para_text = ' '.join(current_paragraph)
                # Ensure ends with punctuation
                if not ends_with_sentence(para_text):
                    para_text += '.'
                output.append(para_text)
                current_paragraph = []
            current_paragraph.append(text)
        elif gap_s >= sentence_pause:
            # Sentence break within paragraph
            if current_paragraph:
                last = current_paragraph[-1]
                if not ends_with_sentence(last) and not is_incomplete(last):
                    current_paragraph[-1] = last + '.'
            current_paragraph.append(text)
        else:
            # Continuation: join with space
            current_paragraph.append(text)

    # Flush remaining
    if current_paragraph:
        para_text = ' '.join(current_paragraph)
        if not ends_with_sentence(para_text):
            para_text += '.'
        output.append(para_text)

    # Join paragraphs
    result = '\n\n'.join(p for p in output if p and p != '\n---\n')
    # Re-insert section breaks properly
    result = re.sub(r'\n\n(\n---\n)\n\n', r'\n\n---\n\n', result)

    return result

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    srt_path = Path(sys.argv[1])
    if not srt_path.exists():
        print(f"File not found: {srt_path}")
        sys.exit(1)

    # Parse options
    sentence_t, para_t, section_t = SENTENCE_PAUSE, PARAGRAPH_PAUSE, SECTION_PAUSE
    skip_intro = False
    output_path = None

    args = sys.argv[2:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg.startswith('--thresholds='):
            parts = arg.split('=')[1].split(',')
            if len(parts) >= 1: sentence_t = float(parts[0])
            if len(parts) >= 2: para_t = float(parts[1])
            if len(parts) >= 3: section_t = float(parts[2])
        elif arg == '--skip-intro':
            skip_intro = True
        elif arg == '-o' and i + 1 < len(args):
            output_path = Path(args[i + 1])
            i += 1
        i += 1

    blocks = parse_srt(srt_path)
    prose = convert_to_prose(blocks, sentence_t, para_t, section_t, skip_intro)

    if output_path:
        output_path.write_text(prose, encoding='utf-8')
        print(f"Wrote {len(prose):,} chars to {output_path}")
    else:
        print(prose)

if __name__ == '__main__':
    main()
