import re
import sys
from io import StringIO

test_input1 = """Join WebStars now for free, at www.web-stars.com 
You can also support our partners:
Internet - www.internet.com
WebSpiders - www.webspiders101.com
Sentinel - www.sentinel.-ko
"""
test_input2 = """Need information about cheap hotels in London?
You can check us at www.london-hotels.co.uk !
We provide the best services in London.
Here are some reviews in some blogs:
London Hotels are awesome! - www.indigo.bloggers.com 
I am very satisfied with their services - ww.ivan.bg
Best Hotel Services! - www.rebel21.sedecrem.moc
"""

#w{3}\.\w+-?\w+\.[a-z]+(\.[a-z]+)?

text = input()
pattern = r"w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+"
valids = []
while text:
    valid_sites = [el.group() for el in re.finditer(pattern,text)]
    if valid_sites:
        valids.extend(valid_sites)
    text = input()

print(*valids,sep="\n")