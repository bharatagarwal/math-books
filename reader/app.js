const BOOKS = [
  {
    id: 'mcs-lectures',
    title: 'MCS Lectures',
    meta: 'MIT 6.042J Fall 2010',
    basePath: 'mcs-lectures',
    chapters: [
      { file: '01 - What is a Proof.md', title: '1. What is a Proof?' },
      { file: '02 - Proof by Contradiction and Induction.md', title: '2. Contradiction & Induction' },
      { file: '03 - Invariants and Strong Induction.md', title: '3. Invariants & Strong Induction' },
      { file: '04 - Number Theory and the GCD.md', title: '4. Number Theory & GCD' },
      { file: 'Appendix - Gödel\'s Incompleteness.md', title: 'Appendix: Undecidability & Gödel' },
    ]
  },
  {
    id: 'dm',
    title: 'Discrete Mathematics',
    meta: 'Lovász & Vesztergombi · Yale, Spring 1999',
    basePath: 'dm',
    chapters: [
      { file: '01 - Introduction.md', title: 'Introduction' },
      { file: '02 - Let us count.md', title: 'Let us count!' },
      { file: '03 - Induction.md', title: 'Induction' },
      { file: '04 - Counting subsets.md', title: 'Counting subsets' },
      { file: '05 - Pascals Triangle.md', title: "Pascal's Triangle" },
      { file: '06 - Fibonacci numbers.md', title: 'Fibonacci numbers' },
      { file: '07 - Combinatorial probability.md', title: 'Combinatorial probability' },
      { file: '08 - Integers divisors and primes.md', title: 'Integers, divisors & primes' },
      { file: '09 - Graphs.md', title: 'Graphs' },
      { file: '10 - Trees.md', title: 'Trees' },
      { file: '11 - Finding the optimum.md', title: 'Finding the optimum' },
      { file: '12 - Matchings in graphs.md', title: 'Matchings in graphs' },
      { file: '13 - Graph coloring.md', title: 'Graph coloring' },
      { file: '14 - A Connecticut class in King Arthurs court.md', title: "King Arthur's Court" },
      { file: '15 - A glimpse of cryptography.md', title: 'A glimpse of cryptography' },
      { file: '16 - One-time pads.md', title: 'One-time pads' },
      { file: '17 - Answers to exercises.md', title: 'Answers to Exercises' },
    ]
  },
  {
    id: 'mcs',
    title: 'Mathematics for Computer Science',
    meta: 'MIT 6.042J',
    basePath: 'mcs/01 - Proofs',
    chapters: [
      { file: '01 - Intro to Proofs.md', title: '1. What is a Proof?' },
      { file: '02 - Proof Methods.md', title: '1.7 Proof Methods' },
      { file: '03 - Well Ordering Principle.md', title: '2. Well Ordering Principle' },
      { file: '04 - Logic & Propositions.md', title: '3. Logical Formulas' },
      { file: '05 - Quantifiers & Predicate Logic.md', title: '3.2 Quantifiers & Predicate Logic' },
      { file: '06 - Sets.md', title: '4. Sets' },
      { file: '07 - Binary Relations.md', title: '4.4 Binary Relations' },
      { file: '08 - Induction.md', title: '5. Induction' },
      { file: '09 - State Machines—Invariants.md', title: '5.4 State Machines' },
      { file: '10 - Recursive Definition.md', title: '6. Recursive Data Types' },
      { file: '11 - Infinite Sets.md', title: '7. Infinite Sets' },
    ]
  },
  {
    id: 'pim',
    title: "Programmer's Intro to Mathematics",
    meta: 'Jeremy Kun',
    basePath: 'pim',
    chapters: [
      { file: '00 - Our Goal.md', title: 'Our Goal' },
      { file: '01 - Like Programming Mathematics has a Culture.md', title: 'Math has a Culture' },
      { file: '02 - Polynomials.md', title: 'Polynomials' },
      { file: '02a - On Pace and Patience.md', title: 'On Pace and Patience' },
      { file: '03 - Sets.md', title: 'Sets' },
      { file: '03a - Variable Names Overloading and Your Brain.md', title: 'Variable Names & Your Brain' },
      { file: '04 - Graphs.md', title: 'Graphs' },
      { file: '04a - The Many Subcultures of Mathematics.md', title: 'Subcultures of Mathematics' },
      { file: '05 - Calculus with One Variable.md', title: 'Calculus with One Variable' },
      { file: '05a - On Types and Tail Calls.md', title: 'On Types and Tail Calls' },
      { file: '06 - Linear Algebra.md', title: 'Linear Algebra' },
      { file: '06a - Live and Learn Linear Algebra Again.md', title: 'Live and Learn Linear Algebra' },
      { file: '07 - Eigenvectors and Eigenvalues.md', title: 'Eigenvectors & Eigenvalues' },
      { file: '07a - Rigor and Formality.md', title: 'Rigor and Formality' },
      { file: '08 - Multivariable Calculus and Optimization.md', title: 'Multivariable Calculus' },
      { file: '08a - The Argument for Big-O Notation.md', title: 'The Argument for Big-O' },
      { file: '09 - Groups.md', title: 'Groups' },
      { file: '09a - A New Interface.md', title: 'A New Interface' },
      { file: '10 - Appendix A - Notation.md', title: 'Appendix A. Notation' },
      { file: '11 - Appendix B - A Summary of Proofs.md', title: 'Appendix B. A Summary of Proofs' },
      { file: '12 - Appendix C - Annotated Resources.md', title: 'Appendix C. Annotated Resources' },
    ]
  },
  {
    id: 'bradfield',
    title: 'Bradfield Math Course',
    meta: 'Mathematics for Computing · Tom Alcorn, 2020',
    basePath: 'bradfield',
    chapters: [
      { file: '00 - Course Outline.md', title: 'Course Outline' },
      { file: '01 - Counting.md', title: '1. Counting' },
      { file: '02 - Probability.md', title: '2. Probability' },
      { file: "03 - Bayes' Rule.md", title: "3. Bayes' Rule" },
      { file: '04 - Logic.md', title: '4. Logic' },
      { file: '05 - Proofs.md', title: '5. Proofs' },
      { file: '06 - Induction and Recursive Data Types.md', title: '6. Induction & Recursion' },
      { file: '07 - Linear Algebra.md', title: '7. Linear Algebra' },
      { file: '08 - Linear Algebra 2.md', title: '8. Linear Algebra 2' },
      { file: '09 - Graph Theory.md', title: '9. Graph Theory' },
      { file: '10 - Number Theory.md', title: '10. Number Theory' },
      { file: '11 - Cryptography.md', title: '11. Cryptography' },
      { file: '12 - Revision and Problem Solving.md', title: '12. Revision & Practice' },
    ]
  },
  {
    id: 'polya',
    title: 'How to Solve It',
    meta: 'Adapted from G. Pólya, 1945',
    basePath: 'polya',
    chapters: [
      { file: '00 - The Method.md', title: 'The Method' },
      { file: '01 - Make the Problem Yours.md', title: 'Make the Problem Yours' },
      { file: '02 - Restate and Represent.md', title: 'Restate and Represent' },
      { file: '03 - Is the Condition Possible.md', title: 'Is the Condition Possible?' },
      { file: '04 - Look for a Related Problem.md', title: 'Look for a Related Problem' },
      { file: '05 - Try Small Cases.md', title: 'Try Small Cases' },
      { file: '06 - Generalize.md', title: 'Generalize' },
      { file: '07 - Vary the Problem.md', title: 'Vary the Problem' },
      { file: '08 - Auxiliary Problems.md', title: 'Auxiliary Problems' },
      { file: '09 - Auxiliary Elements.md', title: 'Auxiliary Elements' },
      { file: '10 - Work Backwards.md', title: 'Work Backwards' },
      { file: '11 - Signs of Progress.md', title: 'Signs of Progress' },
      { file: '12 - Guess Test and Refine.md', title: 'Guess, Test, Refine' },
      { file: '13 - Plausible Reasoning.md', title: 'Plausible Reasoning' },
      { file: '14 - Carry Out the Plan.md', title: 'Carry Out the Plan' },
      { file: '15 - Looking Back.md', title: 'Looking Back' },
      { file: '16 - Style and Practice.md', title: 'Style and Practice' },
      { file: '17 - Problems.md', title: 'Problems' },
    ]
  },
  {
    id: 'mathematical-notation',
    title: 'Mathematical Notation',
    meta: 'Fork of Scheinerman, 2011',
    basePath: 'mathematical-notation',
    chapters: [
      { file: '00 - Preface.md', title: 'Preface' },
      { file: '01 - Letters.md', title: 'Letters' },
      { file: '02 - Collections.md', title: 'Collections' },
      { file: '03 - Logic.md', title: 'Logic' },
      { file: '04 - Numbers.md', title: 'Numbers' },
      { file: '05 - Geometry.md', title: 'Geometry' },
      { file: '06 - Functions.md', title: 'Functions' },
      { file: '07 - Linear Algebra.md', title: 'Linear Algebra' },
      { file: '08 - Calculus.md', title: 'Calculus' },
      { file: '09 - Probability and Statistics.md', title: 'Probability & Statistics' },
      { file: '10 - Approximation.md', title: 'Approximation' },
      { file: '11 - Bibliography.md', title: 'Bibliography' },
      { file: '12 - Chart.md', title: 'Chart' },
      { file: '13 - Notation Index.md', title: 'Notation Index' },
      { file: '14 - Topic Index.md', title: 'Topic Index' },
    ]
  }
];

function bookIndexFromHash() {
  const h = location.hash.replace(/^#/, '');
  if (!h) return -1;
  const parts = h.split('/');
  const bookId = parts[0];
  return BOOKS.findIndex(b => b.id === bookId);
}
function chapterIndexFromHash() {
  const h = location.hash.replace(/^#/, '');
  const parts = h.split('/');
  return parts.length > 1 ? parseInt(parts[1], 10) || 0 : 0;
}
function updateHash() {
  const book = BOOKS[currentBook];
  const newHash = '#' + book.id + '/' + currentChapter;
  if (location.hash !== newHash) {
    history.replaceState(null, '', newHash);
  }
}

let currentBook = bookIndexFromHash() >= 0
  ? bookIndexFromHash()
  : Math.floor(Math.random() * BOOKS.length);
let currentChapter = -1;

// Custom renderer for figures with captions
const renderer = new marked.Renderer();
let currentBasePath = '';

renderer.image = function(token) {
  let { href, title, text } = token;
  if (href && !href.startsWith('http')) {
    const imgBase = currentBasePath ? currentBasePath + '/' : '';
    const fullPath = imgBase + href;
    const encodedPath = fullPath.split('/').map(encodeURIComponent).join('/');
    href = '../markdown/' + encodedPath;
  }
  const img = '<img src="' + href + '" alt="' + (text || '') + '"' + (title ? ' title="' + title + '"' : '') + '>';
  if (text) {
    return '<figure>' + img + '<figcaption>' + text + '</figcaption></figure>';
  }
  return img;
};

renderer.code = function(token) {
  const code = token.text;
  const lang = (token.lang || '').split(' ')[0];
  let highlighted;
  if (lang && hljs.getLanguage(lang)) {
    highlighted = hljs.highlight(code, { language: lang }).value;
  } else {
    highlighted = hljs.highlightAuto(code).value;
  }
  const langClass = lang ? ' class="language-' + lang + '"' : '';
  return '<pre><code' + langClass + '>' + highlighted + '</code></pre>';
};

marked.setOptions({ gfm: true, breaks: false, renderer: renderer });

// GFM footnotes ([^id] refs + [^id]: defs) via the marked-footnote extension.
// It runs inside marked.parse, so the math-masking placeholders in footnote
// definitions pass through untouched and KaTeX renders them afterward.
if (typeof markedFootnote === 'function') {
  marked.use(markedFootnote());
}

function getFullPath(book, file) {
  return book.basePath ? book.basePath + '/' + file : file;
}

let mathStore = [];

function protectMath(md) {
  mathStore = [];
  let id = 0;
  const placeholder = (content) => {
    const key = '\x00MATH' + (id++) + '\x00';
    mathStore.push({ key, content });
    return key;
  };
  // Split on code fences — only protect math outside code blocks
  const parts = md.split(/(^```[\s\S]*?^```)/gm);
  for (let i = 0; i < parts.length; i++) {
    if (parts[i].startsWith('```')) continue;
    let p = parts[i];
    // Protect $$...$$ (display) first, then $...$ (inline)
    p = p.replace(/\$\$([\s\S]*?)\$\$/g, (m) => placeholder(m));
    p = p.replace(/(?<![\\$])\$(?!\$)((?:[^$\\]|\\.)+?)\$/g, (m) => placeholder(m));
    // Protect \[...\] and \(...\)
    p = p.replace(/\\\[([\s\S]*?)\\\]/g, (m) => placeholder(m));
    p = p.replace(/\\\(([\s\S]*?)\\\)/g, (m) => placeholder(m));
    parts[i] = p;
  }
  return parts.join('');
}

function restoreMath(html) {
  for (const { key, content } of mathStore) {
    html = html.split(key).join(content);
  }
  return html;
}

async function processMarkdown(md) {
  md = md.replace(/<!--\s*page\s+(\d+)\s*-->/gi, '<div class="page-marker">Page $1</div>');

  // marked.js renders ![alt](dest) only when dest has no unescaped spaces, but OCR'd
  // figure paths contain them (e.g. "04 - Counting subsets_images/img-0.jpeg"). Wrap any
  // spaced image destination in <> (CommonMark angle-bracket form) so it parses as an image.
  md = md.replace(/(!\[[^\]\n]*\]\()([^)\n<>"]*\s[^)\n"]*)(\))/g, '$1<$2>$3');

  // Carousel markers: <!-- carousel --> ... <!-- endcarousel --> groups the images
  // between them into a single swipeable widget (built after render in buildCarousels).
  md = md.replace(/<!--\s*carousel\s*-->/gi, '\n\n<div class="carousel-start"></div>\n\n');
  md = md.replace(/<!--\s*endcarousel\s*-->/gi, '\n\n<div class="carousel-end"></div>\n\n');

  const includeRe = /<!--\s*include:\s*(.+?)\s*-->/g;
  const matches = [...md.matchAll(includeRe)];
  if (matches.length === 0) return md;

  const fetches = matches.map(async (m) => {
    const path = '../' + m[1].split('/').map(encodeURIComponent).join('/');
    try {
      const resp = await fetch(path);
      if (!resp.ok) return { match: m, code: '# Failed to load: ' + m[1] };
      return { match: m, code: (await resp.text()).trimEnd() };
    } catch {
      return { match: m, code: '# Failed to load: ' + m[1] };
    }
  });

  const results = await Promise.all(fetches);
  // Map file extensions to markdown language hints for syntax highlighting.
  const extLang = { py: 'python', js: 'javascript', ts: 'typescript', lean: 'lean',
    dfy: 'dafny', rs: 'rust', hs: 'haskell', rb: 'ruby', sh: 'bash', zsh: 'bash' };
  for (const { match, code } of results.reverse()) {
    // If the include is already inside a fenced code block, just replace it.
    // Otherwise, auto-wrap in a fence with the right language hint.
    const before = md.slice(0, match.index);
    const after = md.slice(match.index + match[0].length);
    const lastFence = before.lastIndexOf('```');
    const insideFence = lastFence >= 0 &&
      (before.slice(lastFence).match(/^```/gm) || []).length % 2 === 1;
    if (insideFence) {
      md = before + code + after;
    } else {
      const ext = match[1].split('.').pop();
      const lang = extLang[ext] || ext;
      md = before + '```' + lang + '\n' + code + '\n```' + after;
    }
  }
  return md;
}

// Turn each <!-- carousel -->…<!-- endcarousel --> region into a one-at-a-time
// figure carousel with prev/next controls. Runs after KaTeX so captions stay rendered.
function buildCarousels(root) {
  root.querySelectorAll('.carousel-start').forEach(start => {
    const between = [];
    let el = start.nextElementSibling;
    while (el && !(el.classList && el.classList.contains('carousel-end'))) {
      between.push(el);
      el = el.nextElementSibling;
    }
    const end = el;
    const slides = [];
    between.forEach(n => {
      if (n.tagName === 'FIGURE' || n.tagName === 'IMG') { slides.push(n); return; }
      n.querySelectorAll('figure, img').forEach(x => {
        if (x.tagName === 'FIGURE' || (x.tagName === 'IMG' && !x.closest('figure'))) slides.push(x);
      });
    });
    const uniq = [...new Set(slides)];
    if (uniq.length < 2) { start.remove(); if (end) end.remove(); return; }

    const car = document.createElement('div'); car.className = 'carousel';
    const vp = document.createElement('div'); vp.className = 'carousel-viewport';
    uniq.forEach((s, i) => { s.classList.add('carousel-slide'); if (i) s.classList.add('carousel-hidden'); vp.appendChild(s); });
    const nav = document.createElement('div'); nav.className = 'carousel-nav';
    const prev = document.createElement('button'); prev.type = 'button'; prev.className = 'carousel-btn'; prev.setAttribute('aria-label', 'Previous figure'); prev.textContent = '‹';
    const next = document.createElement('button'); next.type = 'button'; next.className = 'carousel-btn'; next.setAttribute('aria-label', 'Next figure'); next.textContent = '›';
    const counter = document.createElement('span'); counter.className = 'carousel-counter';
    nav.append(prev, counter, next); car.append(vp, nav);

    let cur = 0;
    const show = n => {
      cur = (n + uniq.length) % uniq.length;
      uniq.forEach((s, i) => s.classList.toggle('carousel-hidden', i !== cur));
      counter.textContent = (cur + 1) + ' / ' + uniq.length;
    };
    prev.onclick = () => show(cur - 1);
    next.onclick = () => show(cur + 1);
    show(0);

    start.replaceWith(car);
    between.forEach(n => { if (!uniq.includes(n)) n.remove(); });
    if (end) end.remove();
  });
}

// Chapter-opening epigraphs: a blockquote that directly follows the page's H1
// (the chapter title) is an epigraph quote, rendered right-aligned without the
// usual quote bar. Ordinary blockquotes elsewhere are untouched.
function styleEpigraphs(root) {
  root.querySelectorAll('h1 + blockquote').forEach(bq => {
    bq.classList.add('epigraph');
  });
}

// Exercise text for the clipboard: clone the card and swap each rendered KaTeX
// span back to its TeX source ($…$) so the copied text is chat-pasteable.
function exerciseCopyText(card, num) {
  const clone = card.cloneNode(true);
  clone.querySelectorAll('.exercise-copy, .exercise-num').forEach(e => e.remove());
  clone.querySelectorAll('.katex').forEach(k => {
    const tex = k.querySelector('annotation[encoding="application/x-tex"]');
    k.replaceWith(document.createTextNode(tex ? '$' + tex.textContent + '$' : k.textContent));
  });
  return ('Exercise ' + num + ': ' + clone.textContent.trim()).replace(/\n{3,}/g, '\n\n');
}

// Small copy-to-clipboard affordance in the top-right corner of each card.
function addExerciseCopy(card, num) {
  const btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'exercise-copy';
  btn.title = 'Copy exercise';
  btn.setAttribute('aria-label', 'Copy exercise ' + num);
  btn.innerHTML = '<svg width="13" height="13" viewBox="0 0 16 16" fill="currentColor"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"/><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"/></svg>';
  btn.addEventListener('click', () => {
    navigator.clipboard.writeText(exerciseCopyText(card, num))
      .then(() => showToast('Exercise ' + num + ' copied'))
      .catch(() => showToast('Copy failed'));
  });
  card.appendChild(btn);
}

// Mark up exercise/problem blocks as first-class "exercise cards". Runs after
// KaTeX so any math inside the exercise stays rendered. Two shapes are handled:
//   1. dm blockquotes whose first text token is a bold exercise number, e.g.
//      `> **2.5** …` → marked leaves a leading <strong>2.5</strong>.
//   2. MCS problem headings, e.g. `### Problem 6.1.` → an <h3> "Problem 6.1.".
// Ordinary blockquotes (no leading bold number) and ordinary headings are left
// untouched.
function styleExercises(root) {
  // Leading bold number like "2.5", "10", "3.1." (optional trailing dot).
  const numRe = /^\d+(\.\d+)?\.?$/;

  // 1) dm-style exercise blockquotes.
  root.querySelectorAll('blockquote').forEach(bq => {
    const strong = bq.querySelector('strong');
    if (!strong) return;
    // The <strong> must be the very first rendered token of the blockquote
    // (ignoring whitespace), so we don't badge a bolded word mid-sentence.
    const firstP = bq.firstElementChild;
    if (!firstP) return;
    const owner = firstP.querySelector ? firstP.querySelector('strong') : null;
    if (owner !== strong) return;
    // Nothing but whitespace may precede the <strong> inside its paragraph.
    let pre = '';
    for (const node of firstP.childNodes) {
      if (node === strong) break;
      pre += node.textContent || '';
    }
    if (pre.trim() !== '') return;
    const label = strong.textContent.trim();
    if (!numRe.test(label)) return;

    bq.classList.add('exercise');
    const badge = document.createElement('span');
    badge.className = 'exercise-num';
    badge.textContent = label.replace(/\.$/, '');
    // Replace the inline bold number with the badge, tidy a leading space.
    strong.replaceWith(badge);
    const after = badge.nextSibling;
    if (after && after.nodeType === Node.TEXT_NODE) {
      after.textContent = after.textContent.replace(/^\s+/, ' ');
    }
    addExerciseCopy(bq, badge.textContent);
  });

  // 2) MCS-style problem headings ("Problem N.M.").
  const probRe = /^Problem\s+(\d+(?:\.\d+)?)\.?$/;
  root.querySelectorAll('h1, h2, h3, h4, h5, h6').forEach(h => {
    const m = h.textContent.trim().match(probRe);
    if (!m) return;
    h.classList.add('exercise-heading');
    const badge = document.createElement('span');
    badge.className = 'exercise-num';
    badge.textContent = m[1];
    h.textContent = '';
    h.append(badge, document.createTextNode(' Problem'));
  });
}

// Prev / next chapter footer, appended into the rendered content.
function buildChapterNav(pane, idx) {
  const chapters = BOOKS[currentBook].chapters;
  const md = pane.querySelector('.md');
  if (!md || chapters.length < 2) return;

  const nav = document.createElement('nav');
  nav.className = 'chapter-nav';

  const link = (target, dir) => {
    const a = document.createElement('a');
    a.className = 'cn-link' + (dir === 'next' ? ' cn-next' : '');
    a.innerHTML =
      '<span class="cn-label">' + (dir === 'next' ? 'Next →' : '← Previous') +
      '</span><span class="cn-title">' + chapters[target].title + '</span>';
    a.onclick = () => loadChapter(target);
    return a;
  };

  if (idx > 0) nav.appendChild(link(idx - 1, 'prev'));
  if (idx < chapters.length - 1) nav.appendChild(link(idx + 1, 'next'));
  if (nav.childElementCount) md.appendChild(nav);
}


async function loadChapter(idx) {
  currentChapter = idx;
  updateHash();
  const book = BOOKS[currentBook];
  const ch = book.chapters[idx];
  const fullPath = getFullPath(book, ch.file);

  document.querySelectorAll('.nav-item').forEach((el, i) => el.classList.toggle('active', i === idx));

  const pane = document.getElementById('pane');
  pane.innerHTML = '<div class="empty">Loading...</div>';

  const url = '../markdown/' + encodeURIComponent(fullPath).replace(/%2F/g, '/');

  try {
    const resp = await fetch(url);
    if (!resp.ok) throw new Error('HTTP ' + resp.status);

    let md = await resp.text();
    console.log('Loaded markdown:', md.length, 'chars,', md.split('\n').length, 'lines');
    md = await processMarkdown(md);
    md = protectMath(md);
    currentBasePath = book.basePath;

    let html;
    try {
      html = marked.parse(md);
    } catch (e) {
      console.error('Marked parse error:', e);
      pane.innerHTML = '<div class="error">Markdown parse error: ' + e.message + '</div>';
      return;
    }
    html = restoreMath(html);
    pane.innerHTML = '<div class="md">' + html + '</div>';

    try {
      renderMathInElement(pane, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false},
        {left: '\\[', right: '\\]', display: true},
        {left: '\\(', right: '\\)', display: false}
      ],
      throwOnError: false
    });
    } catch (e) {
      console.error('KaTeX render error:', e);
    }

    buildCarousels(pane);
    styleEpigraphs(pane);
    styleExercises(pane);
    buildChapterNav(pane, idx);
    applyReaderSettings();

    const headings = Array.from(pane.querySelectorAll('h2, h3'));
    headings.forEach((h, i) => { h.id = 'h-' + i; });

    const outlineEl = document.getElementById('outline');
    const keyhint = '<div class="keyhint"><kbd>j</kbd>/<kbd>k</kbd> prev/next · <kbd>z</kbd> zen · <kbd>f</kbd> fullscreen</div>';
    const items = headings.slice(1);
    outlineEl.innerHTML = (items.length > 0
      ? '<div class="outline-label">On this page</div>' +
        items.map(h => '<div class="outline-item' + (h.tagName === 'H3' ? ' l3' : '') + '" data-target="' + h.id + '">' + h.textContent + '</div>').join('')
      : '') + keyhint;

    outlineEl.querySelectorAll('.outline-item').forEach(el => {
      el.onclick = () => {
        const target = pane.querySelector('#' + el.dataset.target);
        if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      };
    });

    pane.scrollTop = 0;
    pane.focus({ preventScroll: true });
  } catch (e) {
    pane.innerHTML = '<div class="error">Failed to load: ' + e.message + '</div>';
  }
}

function renderBook() {
  const book = BOOKS[currentBook];
  document.getElementById('title').textContent = book.title;
  document.getElementById('meta').textContent = book.meta;

  const sidebar = document.getElementById('sidebar');
  sidebar.innerHTML = book.chapters.map((ch, i) =>
    '<div class="nav-item" data-idx="' + i + '">' + ch.title + '</div>'
  ).join('');

  sidebar.querySelectorAll('.nav-item').forEach(el => {
    el.onclick = () => loadChapter(+el.dataset.idx);
  });

  const hashCh = chapterIndexFromHash();
  const startCh = (hashCh >= 0 && hashCh < book.chapters.length) ? hashCh : 0;
  loadChapter(startCh);
}

// Zen mode + mobile chrome (auto-hiding top bar, floating toggle)
let zenMode = false;
let mobileChromeHidden = false;
let lastPaneScrollTop = 0;

function isMobileViewport() {
  return window.matchMedia('(max-width: 900px)').matches;
}

function updateMobileZenToggle() {
  const button = document.getElementById('mobileZenToggle');
  if (!button) return;
  button.textContent = zenMode ? 'Nav' : 'Zen';
  button.setAttribute('aria-label', zenMode ? 'Exit zen mode' : 'Enter zen mode');
}

function setMobileChromeHidden(next) {
  mobileChromeHidden = next;
  document.body.classList.toggle('mobile-chrome-hidden', mobileChromeHidden);
}

function setZenMode(next) {
  zenMode = next;
  document.body.classList.toggle('zen', zenMode);
  // Leaving zen on mobile should reveal the chrome, not keep it tucked away.
  if (zenMode) setMobileChromeHidden(false);
  updateMobileZenToggle();
}

function toggleZenMode() {
  setZenMode(!zenMode);
}

// Keyboard shortcuts
document.addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT') return;

  const book = BOOKS[currentBook];

  if (e.key === 'z' || e.key === 'Z') {
    e.preventDefault();
    toggleZenMode();
    return;
  }

  if (e.key === 'f' || e.key === 'F') {
    e.preventDefault();
    if (document.fullscreenElement) {
      document.exitFullscreen();
    } else {
      document.documentElement.requestFullscreen();
    }
    return;
  }

  if (e.key === 'k' && currentChapter > 0) {
    e.preventDefault();
    loadChapter(currentChapter - 1);
  }

  if (e.key === 'j' && currentChapter < book.chapters.length - 1) {
    e.preventDefault();
    loadChapter(currentChapter + 1);
  }
});

// Mobile reading controls — font size & line height (persisted per session)
let readerFontSize = parseFloat(localStorage.getItem('mr-fs') || '15');
let readerLineHeight = parseFloat(localStorage.getItem('mr-lh') || '1.7');

function applyReaderSettings() {
  const md = document.querySelector('.md');
  if (!md) return;
  md.style.fontSize = readerFontSize + 'px';
  md.style.lineHeight = readerLineHeight;
}

function showToast(msg) {
  const t = document.getElementById('mtToast');
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(t._timer);
  t._timer = setTimeout(() => t.classList.remove('show'), 1200);
}

function changeFontSize(d) {
  readerFontSize = Math.max(12, Math.min(22, +(readerFontSize + d).toFixed(1)));
  localStorage.setItem('mr-fs', readerFontSize);
  applyReaderSettings();
  showToast(readerFontSize + 'px');
}

function changeLineHeight(d) {
  readerLineHeight = Math.max(1.2, Math.min(2.4, +(readerLineHeight + d).toFixed(2)));
  localStorage.setItem('mr-lh', readerLineHeight);
  applyReaderSettings();
  showToast(readerLineHeight + ' line height');
}

document.getElementById('mtFontDown').addEventListener('click', () => changeFontSize(-0.5));
document.getElementById('mtFontUp').addEventListener('click', () => changeFontSize(0.5));
document.getElementById('mtLhDown').addEventListener('click', () => changeLineHeight(-0.1));
document.getElementById('mtLhUp').addEventListener('click', () => changeLineHeight(0.1));

// Collapsible toolbar toggle
const toolbar = document.getElementById('mobileToolbar');
document.getElementById('mtToggle').addEventListener('click', () => {
  toolbar.classList.toggle('expanded');
});

// Mobile zen toggle button
document.getElementById('mobileZenToggle').addEventListener('click', toggleZenMode);

// On mobile, tuck the top bar away as you scroll down, reveal it scrolling up.
document.getElementById('pane').addEventListener('scroll', () => {
  const pane = document.getElementById('pane');
  const top = pane.scrollTop;
  if (isMobileViewport() && !zenMode) {
    if (top <= 24) {
      setMobileChromeHidden(false);
    } else {
      const delta = top - lastPaneScrollTop;
      if (delta > 10) setMobileChromeHidden(true);
      else if (delta < -10) setMobileChromeHidden(false);
    }
  }
  lastPaneScrollTop = top;
});

// Reaching the desktop breakpoint should always restore the chrome.
window.addEventListener('resize', () => {
  if (!isMobileViewport()) setMobileChromeHidden(false);
});

// Init
const sel = document.getElementById('bookSelect');
sel.innerHTML = BOOKS.map((b, i) => '<option value="' + i + '">' + b.title + '</option>').join('');
sel.value = currentBook;
sel.onchange = () => { currentBook = +sel.value; currentChapter = 0; updateHash(); renderBook(); };
renderBook();
updateMobileZenToggle();
