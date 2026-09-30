"""Regenerate CBETA reading texts; requires opencc-python-reimplemented.
Keeps Diamond Sutra navigation from the supplied original; includes verse blocks.
"""
from pathlib import Path
import xml.etree.ElementTree as ET
import re,difflib
from opencc import OpenCC
root=Path(__file__).resolve().parents[1];cc=OpenCC('t2s'); ns={'t':'http://www.tei-c.org/ns/1.0','cb':'http://www.cbeta.org/ns/1.0'}
def clean(node):
 tag=node.tag.split('}')[-1]
 if tag in ('note','mulu','head','rdg','fw'): return ''
 if tag=='app':
  lem=node.find('t:lem',ns);return clean(lem) if lem is not None else ''
 s=node.text or ''
 for ch in node:
  s+=clean(ch)+(ch.tail or '')
 return s

def text(node): return cc.convert(re.sub(r'\s+','',clean(node)))
p=root/'classics/diamond-sutra/original.txt';old=(p.parent/'source/user-original.txt').read_text(); parts=re.split(r'(金刚经[ \t\u00a0]+第[^\n]+\n)',old)[1:]; headings=parts[::2]; bodies=parts[1::2]
xml=ET.parse(root/'classics/diamond-sutra/source/T08n0235.xml');jing=xml.find('.//cb:div[@type="jing"]',ns)
# Preserve canonical paragraph boundaries, including verse blocks.
blocks=[text(e) for e in jing if e.tag.split('}')[-1] in ('p','lg')]
canonical='\n\n'.join(blocks)
def stripped(s):return ''.join(c for c in s if '\u3400'<=c<='\u9fff')
a=''.join(stripped(b) for b in bodies);b=stripped(canonical)
matcher=difflib.SequenceMatcher(None,a,b,autojunk=False);matches=matcher.get_matching_blocks()
positions=[i for i,c in enumerate(canonical) if '\u3400'<=c<='\u9fff']
starts=[];offset=0
for body in bodies:
 block=next(m for m in matches if m.a<=offset<m.a+m.size or m.a>=offset)
 pos=block.b+max(0,offset-block.a)
 raw=positions[pos]
 while raw>0 and canonical[raw-1] in '「『':raw-=1
 starts.append(raw);offset+=len(stripped(body))
assert len(starts)==32 and starts[0]==0 and starts==sorted(set(starts))
new='《金刚经》\n'+''.join(h+canonical[starts[i]:starts[i+1] if i+1<len(starts) else len(canonical)].strip()+'\n\n' for i,h in enumerate(headings))
assert stripped(''.join(re.split(r'金刚经[ \t\u00a0]+第[^\n]+\n',new)[1:]))==b
p.write_text(new)
print('金刚经32品已采用CBETA现代标点，分品正文完整保留底本。')
# Retain the existing ten chapter headings and restore verse elements skipped before.
p=root/'classics/platform-sutra/original.txt';heads=re.findall(r'^## .+$',p.read_text(),re.M)
xml=ET.parse(root/'classics/platform-sutra/source/T48n2008.xml')
divs=[]
for div in xml.findall('.//cb:div',ns):
 m=div.find('cb:mulu',ns)
 if m is not None and re.match(r'^\d+ ',m.text or ''): divs.append(div)
assert len(divs)==len(heads)==10
out=[]
for h,div in zip(heads,divs):
 body=[]
 for e in div:
  tag=e.tag.split('}')[-1]
  if tag=='p':body.append(text(e))
  elif tag=='lg':body.append('\n'.join(text(l) for l in e.findall('t:l',ns)))
 out.append(h+'\n'+'\n\n'.join(body))
p.write_text('\n\n'.join(out)+'\n')
print('坛经十品已恢复CBETA偈颂及其原有标点。')
