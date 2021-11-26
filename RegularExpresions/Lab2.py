import re
import sys
from io import StringIO

test_input = "+359 2 222 2222,359-2-222-2222, +359/2/222/2222, " \
             "+359-2 222 2222 +359 2-222-2222, +359-2-222-222, +359-2-222-22222 +359-2-222-2222"

sys.stdin = StringIO(test_input)

text = input()
pattern = r"(\+359 [0-9] [0-9]{3} [0-9]{4}\b)|(\+359-[0-9]-[0-9]{3}-([0-9]{4}\b))"

valid_numbers = [obj.group() for obj in re.finditer(pattern,text)]


print(", ".join(valid_numbers))


