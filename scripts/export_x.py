#!/usr/bin/env python3
"""Export an English Pages essay as Markdown and a rich-text copy page for X."""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

from export_wechat import parse_frontmatter, render_inline

ROOT = Path(__file__).resolve().parents[1]


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
:root{color-scheme:light;--pine:#18372f;--ivory:#f6f3eb;--copper:#ab8966}
*{box-sizing:border-box}body{margin:0;background:var(--ivory);color:#354039;
font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif}
main{max-width:760px;margin:40px auto;padding:36px;background:#fff;border-top:4px solid var(--pine)}
.tools{padding-bottom:26px;border-bottom:1px solid #e5e8e0;margin-bottom:30px}
.label{font-size:12px;letter-spacing:2px;color:#826c51}.instructions{font-size:14px;line-height:1.7;color:#68736a}
.actions{display:flex;gap:10px;flex-wrap:wrap}button,.cover-link{border:1px solid #c8d2c7;
border-radius:6px;padding:10px 15px;background:#fff;color:var(--pine);font:inherit;font-size:14px;cursor:pointer}
button:first-child{background:var(--pine);color:#fff;border-color:var(--pine)}
button:hover,.cover-link:hover{box-shadow:0 2px 8px #17201818}.cover-link{text-decoration:none}
#copy-status{min-height:22px;margin:12px 0 0;color:var(--pine);font-size:13px}
h1{font-size:32px;line-height:1.25;margin:0 0 30px;color:var(--pine)}
#article-body{font-size:17px;line-height:1.85}p{margin:0 0 20px}
h2{font-size:23px;line-height:1.4;margin:36px 0 18px;color:var(--pine)}
h3{font-size:20px;line-height:1.4;margin:28px 0 16px;color:var(--pine)}
strong{font-weight:700;color:var(--pine)}a{color:var(--pine);text-decoration:underline}
blockquote{margin:24px 0;padding-left:18px;border-left:3px solid var(--copper)}
@media(max-width:600px){main{margin:0;padding:24px 20px}h1{font-size:27px}h2{font-size:21px}}
@media print{.tools{display:none}body{background:#fff}main{margin:0;border:0;padding:0}}
</style></head><body><main>
<header class="tools">
<p class="label">WULAI · X ARTICLES</p>
<p class="instructions">Copy the title into the title field, then copy the formatted body into the X Articles editor. Upload the English cover separately (5:2). X controls the final typography; check headings and emphasis after pasting.</p>
<div class="actions"><button type="button" id="copy-body">Copy formatted body</button>
<button type="button" id="copy-title">Copy title</button>
<a class="cover-link" href="images/cover-en.png" download>English cover · 5:2</a></div>
<p id="copy-status" role="status" aria-live="polite"></p>
<noscript><p class="instructions">Select the title or article body below and copy it using your browser.</p></noscript>
</header><h1 id="article-title">__TITLE__</h1>
<article id="article-body">__BODY__</article>
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
    directory = ROOT / "articles" / slug
    page = PAGE.replace("__TITLE__", html.escape(title)).replace("__BODY__", markup)
    (directory / "x.html").write_text(page, encoding="utf-8")
    (directory / "x.md").write_text(f"# {title}\n\n{body}\n", encoding="utf-8")
    print(f"Generated x.html and x.md for {slug}.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="Article directory name, e.g. YYYY-MM-DD-short-title")
    export(parser.parse_args().slug)


if __name__ == "__main__":
    main()
