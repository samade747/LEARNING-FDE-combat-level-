// P4-P5 scaffold: zero-dependency static-site build, standing in for the real
// Next.js+Fumadocs human projection (see README "Real Fumadocs" section for
// the actual `npx create-fumadocs-app` path). No npm install needed to run this.
//
// Reads knowledge/*.md (frontmatter + body), fails the build if any required
// provenance field is missing (P4's "converted with provenance" requirement),
// then writes static/index.html (nav) + static/<slug>.html (one page per doc).

const fs = require("fs");
const path = require("path");

const KNOWLEDGE_DIR = path.join(__dirname, "knowledge");
const OUT_DIR = path.join(__dirname, "static");
const REQUIRED_FIELDS = ["title", "source", "owner", "version", "effective_period", "authority_kind"];

function parseFrontmatter(raw) {
  const match = raw.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) throw new Error("no frontmatter block found");
  const [, fmText, body] = match;
  const fm = {};
  for (const line of fmText.split("\n")) {
    const idx = line.indexOf(":");
    if (idx === -1) continue;
    fm[line.slice(0, idx).trim()] = line.slice(idx + 1).trim();
  }
  return { fm, body: body.trim() };
}

function escapeHtml(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

// Minimal markdown -> HTML: headings, paragraphs, bullet lists. Enough for
// this scaffold's docs; a real Fumadocs site uses MDX and a real renderer.
function renderMarkdown(md) {
  const lines = md.split("\n");
  let html = "";
  let inList = false;
  for (const line of lines) {
    const h = line.match(/^(#{1,3})\s+(.*)$/);
    if (h) {
      if (inList) { html += "</ul>\n"; inList = false; }
      const level = h[1].length;
      html += `<h${level}>${escapeHtml(h[2])}</h${level}>\n`;
      continue;
    }
    const li = line.match(/^-\s+(.*)$/);
    if (li) {
      if (!inList) { html += "<ul>\n"; inList = true; }
      html += `<li>${escapeHtml(li[1])}</li>\n`;
      continue;
    }
    if (line.trim() === "") {
      if (inList) { html += "</ul>\n"; inList = false; }
      continue;
    }
    if (inList) { html += "</ul>\n"; inList = false; }
    html += `<p>${escapeHtml(line)}</p>\n`;
  }
  if (inList) html += "</ul>\n";
  return html;
}

function build() {
  const files = fs.readdirSync(KNOWLEDGE_DIR).filter((f) => f.endsWith(".md"));
  if (files.length < 5) {
    throw new Error(`Milestone 1 needs 5+ governed documents, found ${files.length}`);
  }

  const docs = [];
  for (const file of files) {
    const raw = fs.readFileSync(path.join(KNOWLEDGE_DIR, file), "utf8");
    const { fm, body } = parseFrontmatter(raw);
    const missing = REQUIRED_FIELDS.filter((f) => !fm[f]);
    if (missing.length > 0) {
      throw new Error(`${file}: missing required provenance field(s): ${missing.join(", ")}`);
    }
    const slug = file.replace(/\.md$/, "");
    docs.push({ slug, fm, body });
  }

  fs.mkdirSync(OUT_DIR, { recursive: true });

  const navLinks = docs
    .map((d) => `    <li><a href="${d.slug}.html">${escapeHtml(d.fm.title)}</a></li>`)
    .join("\n");

  const indexHtml = `<!doctype html>
<html><head><meta charset="utf-8"><title>Vertical SoR — Human Projection (scaffold)</title></head>
<body>
  <h1>Vertical SoR — Human Projection (P4-P5 scaffold)</h1>
  <p>${docs.length} governed documents, each with a provenance block (source, owner, version, effective period, authority kind).</p>
  <ul>
${navLinks}
  </ul>
</body></html>`;
  fs.writeFileSync(path.join(OUT_DIR, "index.html"), indexHtml);

  for (const d of docs) {
    const provRows = REQUIRED_FIELDS
      .map((f) => `      <tr><td>${f}</td><td>${escapeHtml(d.fm[f])}</td></tr>`)
      .join("\n");
    const pageHtml = `<!doctype html>
<html><head><meta charset="utf-8"><title>${escapeHtml(d.fm.title)}</title></head>
<body>
  <p><a href="index.html">&larr; all documents</a></p>
  <h1>${escapeHtml(d.fm.title)}</h1>
  <table border="1" cellpadding="4">
    <tr><th colspan="2">Provenance</th></tr>
${provRows}
  </table>
${renderMarkdown(d.body)}
</body></html>`;
    fs.writeFileSync(path.join(OUT_DIR, `${d.slug}.html`), pageHtml);
  }

  console.log(`Built ${docs.length} pages into ${OUT_DIR}`);
  return docs.length;
}

if (require.main === module) {
  try {
    build();
  } catch (err) {
    console.error("BUILD FAILED:", err.message);
    process.exit(1);
  }
}

module.exports = { build, parseFrontmatter, REQUIRED_FIELDS };
