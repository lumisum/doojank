"""Build the scripture-only webfont: python build_sutra_font.py source.ttf.

Requires fonttools and brotli. Includes original text and chapter titles from
all classics. Rebuild after adding or changing scripture source text.
"""
from pathlib import Path
import sys
from fontTools import subset
from fontTools.ttLib import TTFont

root = Path(__file__).resolve().parents[1]
text = "".join(p.read_text() for p in (root / "classics").rglob("original.txt"))
text += "金刚般若波罗蜜经般若波罗蜜多心经六祖坛经传习录"
font = TTFont(sys.argv[1])
options = subset.Options()
options.flavor = "woff2"
options.name_IDs = [0, 1, 2, 3, 4, 5, 6, 13, 14]
options.name_legacy = True
options.name_languages = ["*"]
subsetter = subset.Subsetter(options=options)
subsetter.populate(text=text)
subsetter.subset(font)
# Use a new family name for this modified, scripture-specific subset.
for record in font["name"].names:
    if record.nameID in (1, 3, 4, 6):
        value = "WulaiSutraKai-Regular" if record.nameID in (3, 6) else "Wulai Sutra Kai"
        record.string = value.encode(record.getEncoding())
font.flavor = "woff2"
font.save(root / "assets/fonts/wulai-sutra-kai.woff2")
