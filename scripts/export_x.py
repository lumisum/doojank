#!/usr/bin/env python3
"""Export an English Pages essay as Markdown and a rich-text copy page for X."""

from __future__ import annotations

import argparse
import html
import posixpath
import re
from pathlib import Path
from urllib.parse import urlsplit

from export_wechat import caption_copy_script, parse_frontmatter

ROOT = Path(__file__).resolve().parents[1]


X_INLINE_RE = re.compile(r"\*\*(.+?)\*\*|\*(.+?)\*|~~(.+?)~~|`([^`]+)`|\[([^\]]+)\]\(([^)]+)\)")


def render_inline(text: str) -> str:
    """Platform-oriented semantics, independent of the WeChat colour renderer."""
    parts = []
    cursor = 0
    for match in X_INLINE_RE.finditer(text):
        parts.append(html.escape(text[cursor:match.start()], quote=False))
        strong, emphasis, strike, code, label, url = match.groups()
        if strong is not None:
            parts.append(f"<strong>{html.escape(strong, quote=False)}</strong>")
        elif emphasis is not None:
            parts.append(f"<em>{html.escape(emphasis, quote=False)}</em>")
        elif strike is not None:
            parts.append(f"<s>{html.escape(strike, quote=False)}</s>")
        elif code is not None:
            parts.append(html.escape(code, quote=False))
        else:
            parts.append(f'<a href="{html.escape(url, quote=True)}">{html.escape(label, quote=False)}</a>')
        cursor = match.end()
    parts.append(html.escape(text[cursor:], quote=False))
    return "".join(parts)


def body_markup(body: str) -> str:
    blocks = []
    for block in re.split(r"\n\s*\n", body.strip()):
        # Keep semantic rich text, without the colours used by WeChat exports.
        if re.search(r"!\[[^\]]*\]\([^)]*\)", block) or "<img" in block.lower():
            raise ValueError("Remove interior images from the English edition before exporting.")
        heading = re.fullmatch(r"(#{1,3})\s+(.+)", block)
        if heading:
            level = max(2, len(heading[1]))
            blocks.append(f"<h{level}>{render_inline(heading[2])}</h{level}>")
        elif block.startswith("> "):
            text = " ".join(re.sub(r"^>\s?", "", line) for line in block.splitlines())
            blocks.append(f"<blockquote><p>{render_inline(text)}</p></blockquote>")
        elif all(re.match(r"^[-*]\s+", line) for line in block.splitlines()):
            items = "".join(f"<li>{render_inline(line[2:])}</li>" for line in block.splitlines())
            blocks.append(f"<ul>{items}</ul>")
        elif all(re.match(r"^\d+[.)]\s+", line) for line in block.splitlines()):
            items = []
            for line in block.splitlines():
                text = re.sub(r"^\d+[.)]\s+", "", line)
                items.append(f"<li>{render_inline(text)}</li>")
            blocks.append("<ol>" + "".join(items) + "</ol>")
        else:
            text = " ".join(line.strip() for line in block.splitlines())
            blocks.append(f"<p>{render_inline(text)}</p>")
    return re.sub(r' style="[^"]*"', "", "\n".join(blocks))


PAGE = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__ · X article</title>
<style>
:root{color-scheme:dark;--pine:#62d9ff;--ivory:#09111f;--copper:#a793ff;--ink:#e6edf9;--muted:#98abc5;--line:#29415d}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at 80% 0,#172a46,transparent 55%),var(--ivory);color:#ced9e9;
font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif}
main{max-width:760px;margin:40px auto;padding:36px;background:#0f1b2e;border:1px solid var(--line);border-top:3px solid var(--pine);border-radius:14px;box-shadow:inset 0 1px #ffffff12,0 20px 55px #0005}
.tools{padding-bottom:26px;border-bottom:1px solid var(--line);margin-bottom:30px}
.label{font-size:12px;letter-spacing:2px;color:var(--pine)}.instructions{font-size:14px;line-height:1.7;color:var(--muted)}
.actions{display:flex;gap:10px;flex-wrap:wrap}button,.cover-link{border:1px solid var(--line);
border-radius:8px;padding:10px 15px;background:linear-gradient(145deg,#203752,#14253b);color:#c9eeff;font:inherit;font-size:14px;cursor:pointer;box-shadow:inset 0 1px #ffffff12,0 4px 12px #0002}
button:first-child{background:var(--pine);color:#09111f;border-color:var(--pine)}
button:hover,.cover-link:hover{border-color:var(--pine);box-shadow:0 5px 16px #62d9ff15}.cover-link{text-decoration:none}
button:focus-visible,a:focus-visible{outline:2px solid var(--pine);outline-offset:4px}
#copy-status{min-height:22px;margin:12px 0 0;color:var(--pine);font-size:13px}
h1{font-size:32px;line-height:1.3;margin:0 0 30px;color:var(--ink)}
#article-body{font-size:17px;line-height:1.85}p{margin:0 0 22px}
#article-body>p:first-child{font-size:19px;line-height:1.8;color:var(--ink)}
#article-body>p:last-child{margin-bottom:0}
ul,ol{padding-left:1.5em;margin:24px 0}li{padding-left:.25em;margin:0 0 10px}
.copy-page-signature{margin-top:36px;padding-top:18px;border-top:1px solid var(--line);font-size:11px;color:var(--muted);letter-spacing:.08em}
h2{font-size:23px;line-height:1.4;margin:36px 0 18px;color:var(--ink)}
h3{font-size:20px;line-height:1.4;margin:28px 0 16px;color:var(--ink)}
strong{font-weight:700;color:var(--pine)}a{color:var(--pine);text-decoration:underline}
blockquote{margin:24px 0;padding-left:18px;border-left:3px solid var(--copper)}
@media(max-width:600px){main{margin:0;padding:24px 20px;border-radius:0}h1{font-size:27px}h2{font-size:21px}}
@media print{.tools{display:none}body,main{background:#fff;color:#111}main{margin:0;border:0;padding:0;box-shadow:none}h1,h2,h3,strong,a{color:#111}}
</style></head><body><main>
<header class="tools">
<p class="label">WULAI · PERSONAL JOURNAL</p>
<p class="instructions">Copy the title into the title field, then copy the formatted body into the X Articles editor. Upload the English cover separately (5:2). X controls the final typography; check headings and emphasis after pasting.</p>
<div class="actions"><button type="button" id="copy-body">Copy formatted body</button>
<button type="button" id="copy-title">Copy title</button>
<button type="button" id="copy-caption">Copy caption</button>
<a class="cover-link" href="__COVER__" download>English cover · 5:2</a></div>
<p id="copy-status" role="status" aria-live="polite"></p>
<noscript><p class="instructions">Select the title or article body below and copy it using your browser.</p></noscript>
</header><h1 id="article-title">__TITLE__</h1>
<aside style="padding:18px 20px;margin-bottom:28px;background:#162b45;border-left:3px solid var(--copper);">
<p class="label">ARTICLE CAPTION</p><p id="article-caption" style="margin-bottom:0;font-size:15px;line-height:1.7;">__CAPTION__</p>
<p id="caption-status" role="status" aria-live="polite" style="margin:10px 0 0;font-size:13px;color:var(--pine);"></p></aside>
<article id="article-body">__BODY__</article>
<footer class="copy-page-signature">Stay curious. Keep thinking. · Wulai</footer>
</main><script>
const status = document.getElementById('copy-status');
async function copyArticle(includeTitle) {
  const element = document.getElementById(includeTitle ? 'article-title' : 'article-body');
  const plain = element.innerText;
  const markup = element.innerHTML;
  try {
    if (!navigator.clipboard) throw new Error('Use browser copy');
    if (includeTitle) await navigator.clipboard.writeText(plain);
    else await navigator.clipboard.write([new ClipboardItem({
      'text/html': new Blob([markup], {type:'text/html'}),
      'text/plain': new Blob([plain], {type:'text/plain'})
    })]);
    status.textContent = includeTitle ? 'Title copied.' : 'Formatted body copied. Check formatting in X after pasting.';
    return;
  } catch (error) {
    // Native copy supports locally opened files without the clipboard API.
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(element);
    selection.removeAllRanges();
    selection.addRange(range);
    let copied = false;
    const listener = event => {
      if (!event.clipboardData) return;
      event.clipboardData.setData('text/plain', plain);
      if (!includeTitle) event.clipboardData.setData('text/html', markup);
      event.preventDefault();
      copied = true;
    };
    document.addEventListener('copy', listener);
    try { copied = document.execCommand('copy') && copied; } catch (_) { copied = false; }
    finally { document.removeEventListener('copy', listener); }
    status.textContent = copied
      ? (includeTitle ? 'Title copied.' : 'Formatted body copied. Check formatting in X after pasting.')
      : 'Text selected. Press ⌘C on Mac or Ctrl+C on Windows to copy.';
  }
}
document.getElementById('copy-body').addEventListener('click', () => copyArticle(false));
document.getElementById('copy-title').addEventListener('click', () => copyArticle(true));
</script></body></html>
"""


def export(slug: str) -> None:
    if Path(slug).name != slug:
        raise ValueError("Provide an article directory name, not a path.")
    source = ROOT / "en" / "articles" / slug / "index.md"
    metadata, body = parse_frontmatter(source.read_text(encoding="utf-8"))
    if metadata.get("lang") != "en":
        raise ValueError("X exports require the English edition.")
    markup = body_markup(body)
    title = metadata["title"]
    summary = metadata.get("summary", "")
    if len(summary) > 256:
        raise ValueError(f"English caption must be at most 256 characters, including spaces and punctuation; got {len(summary)}.")
    directory = ROOT / "articles" / slug
    cover = metadata.get("cover", f"/articles/{slug}/images/cover-en.png")
    parsed_cover = urlsplit(cover)
    if not parsed_cover.scheme and not parsed_cover.netloc and parsed_cover.path.startswith("/"):
        local_cover = posixpath.relpath(parsed_cover.path.lstrip("/"), f"articles/{slug}")
        cover = parsed_cover._replace(path=local_cover).geturl()
    page = (
        PAGE.replace("__TITLE__", html.escape(title))
        .replace("__COVER__", html.escape(cover, quote=True))
        .replace("__CAPTION__", html.escape(summary))
        .replace("__BODY__", markup)
        .replace("</body>", caption_copy_script() + "</body>")
    )
    (directory / "x.html").write_text(page, encoding="utf-8")
    (directory / "x.md").write_text(f"# {title}\n\n{body}\n", encoding="utf-8")
    print(f"Generated x.html and x.md for {slug}.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="Article directory name, e.g. YYYY-MM-DD-short-title")
    export(parser.parse_args().slug)


if __name__ == "__main__":
    main()
