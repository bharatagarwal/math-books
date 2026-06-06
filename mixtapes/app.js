// Mixtapes — a small blog over markdown files in markdown/mixtapes/.
// Index lists posts newest-first; #<slug> renders one post. Chapter links
// inside posts point at the reader (../reader/#book/idx) as plain links.

const POSTS = [
  // newest first
  {
    file: 'foundations.md',
    title: 'Foundations Mix: pimbook × Mathematical Notation',
    date: '2026-06-06',
    blurb: 'Kun’s course and Scheinerman’s phrasebook, read together: each notation chapter taken as a short preparation for the pimbook chapter that depends on it.',
  },
];

const content = document.getElementById('content');

// --- markdown pipeline (mirrors the reader: mask math, parse, unmask, KaTeX) ---
let mathStore = [];
function protectMath(md) {
  mathStore = [];
  let id = 0;
  const placeholder = (c) => {
    const key = '\x00MATH' + (id++) + '\x00';
    mathStore.push({ key, content: c });
    return key;
  };
  const parts = md.split(/(^```[\s\S]*?^```)/gm);
  for (let i = 0; i < parts.length; i++) {
    if (parts[i].startsWith('```')) continue;
    parts[i] = parts[i]
      .replace(/\$\$[\s\S]+?\$\$/g, placeholder)
      .replace(/\$[^$\n]+?\$/g, placeholder);
  }
  return parts.join('');
}
function restoreMath(html) {
  for (const { key, content } of mathStore) html = html.replace(key, () => content);
  return html;
}

function postBySlug(slug) {
  return POSTS.find(p => p.file.replace(/\.md$/, '') === slug);
}

function fmtDate(iso) {
  return new Date(iso + 'T00:00:00').toLocaleDateString('en-US',
    { year: 'numeric', month: 'long', day: 'numeric' });
}

function renderIndex() {
  document.title = 'Mixtapes';
  const posts = [...POSTS].sort((a, b) => b.date.localeCompare(a.date));
  content.innerHTML = posts.map(p =>
    '<div class="mx-post">' +
      '<div class="mx-date">' + fmtDate(p.date) + '</div>' +
      '<a class="mx-title" href="#' + p.file.replace(/\.md$/, '') + '">' + p.title + '</a>' +
      '<div class="mx-blurb">' + p.blurb + '</div>' +
    '</div>'
  ).join('') || '<div class="mx-blurb">No mixtapes yet.</div>';
  window.scrollTo(0, 0);
}

async function renderPost(post) {
  document.title = post.title + ' · Mixtapes';
  let md;
  try {
    const resp = await fetch('../markdown/mixtapes/' + encodeURIComponent(post.file));
    if (!resp.ok) throw new Error(resp.status);
    md = await resp.text();
  } catch (e) {
    content.innerHTML = '<div class="error">Failed to load: ' + post.file + '</div>';
    return;
  }
  let html;
  try {
    html = marked.parse(protectMath(md));
  } catch (e) {
    content.innerHTML = '<div class="error">Markdown parse error: ' + e.message + '</div>';
    return;
  }
  content.innerHTML =
    '<a class="mx-back" href="#">← All mixtapes</a>' +
    '<div class="md">' + restoreMath(html) + '</div>';
  const h1 = content.querySelector('.md h1');
  if (h1) h1.insertAdjacentHTML('afterend', '<div class="mx-meta">' + fmtDate(post.date) + '</div>');
  try {
    renderMathInElement(content, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '$', right: '$', display: false },
      ],
      throwOnError: false,
    });
  } catch (e) { console.error('KaTeX render error:', e); }
  content.querySelectorAll('pre code').forEach(el => hljs.highlightElement(el));
  window.scrollTo(0, 0);
}

function route() {
  const slug = location.hash.replace(/^#/, '');
  const post = slug && postBySlug(slug);
  if (post) renderPost(post); else renderIndex();
}

window.addEventListener('hashchange', route);
route();
