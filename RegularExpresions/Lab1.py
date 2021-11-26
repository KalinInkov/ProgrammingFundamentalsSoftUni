import re

import sys
from io import  StringIO

test_input ="Peter Smith, peter smith, Peter smith, " \
            "peter Smith, PEter Smith, Peter SmIth, Lily Everett"

sys.stdin= StringIO(test_input)

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
text = input()
print(' '.join(re.findall(pattern,text)))



# for name in text:
#     match = re.match(pattern,name)
#     if match:
#         valid_names.append(match.group())



