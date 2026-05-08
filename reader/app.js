const BOOKS = [
  {
    id: 'mcs-lectures',
    title: 'MCS Lectures',
    meta: 'MIT 6.042J Fall 2010',
    basePath: 'mcs-lectures',
    chapters: [
      { file: '01 - What is a Proof.md', title: '1. What is a Proof?' },
      { file: '02 - Proof by Contradiction and Induction.md', title: '2. Contradiction & Induction' },
      { file: '03 - Gödel\'s Incompleteness.md', title: '3. Undecidability & Gödel' },
      { file: '04 - Invariants and Strong Induction.md', title: '4. Invariants & Strong Induction' },
      { file: '05 - Number Theory and the GCD.md', title: '5. Number Theory & GCD' },
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
      { file: '01 - Like Programming Mathematics has a Culture.md', title: '1. Math has a Culture' },
      { file: '02 - Polynomials.md', title: '2. Polynomials' },
    ]
  },
  {
    id: 'outline',
    title: 'Bradfield Math Course',
    meta: 'June 2020',
    basePath: '',
    chapters: [
      { file: 'math-2020-06-outline.md', title: 'Course Outline' },
    ]
  }
];

let currentBook = 0;
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
  // Protect $$...$$ (display) first, then $...$ (inline)
  md = md.replace(/\$\$([\s\S]*?)\$\$/g, (m) => placeholder(m));
  md = md.replace(/(?<![\\$])\$(?!\$)((?:[^$\\]|\\.)+?)\$/g, (m) => placeholder(m));
  // Protect \[...\] and \(...\)
  md = md.replace(/\\\[([\s\S]*?)\\\]/g, (m) => placeholder(m));
  md = md.replace(/\\\(([\s\S]*?)\\\)/g, (m) => placeholder(m));
  return md;
}

function restoreMath(html) {
  for (const { key, content } of mathStore) {
    html = html.split(key).join(content);
  }
  return html;
}

function processMarkdown(md) {
  md = md.replace(/<!--\s*page\s+(\d+)\s*-->/gi, '<div class="page-marker">Page $1</div>');
  return md;
}


async function loadChapter(idx) {
  currentChapter = idx;
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
    md = processMarkdown(md);
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

  loadChapter(0);
}

// Keyboard shortcuts
document.addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT') return;

  const book = BOOKS[currentBook];

  if (e.key === 'z' || e.key === 'Z') {
    e.preventDefault();
    document.body.classList.toggle('zen');
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

// Init
const sel = document.getElementById('bookSelect');
sel.innerHTML = BOOKS.map((b, i) => '<option value="' + i + '">' + b.title + '</option>').join('');
sel.onchange = () => { currentBook = +sel.value; renderBook(); };
renderBook();
