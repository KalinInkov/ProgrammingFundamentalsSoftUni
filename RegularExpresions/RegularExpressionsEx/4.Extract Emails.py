import re
# import sys
# from io import StringIO
#
#
# test_input1 = "Please contact us at: support@github.com."
# test_input2 = "Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information."
# test_input3 = "Many users @ SoftUni confuse email addresses. We @ Softuni.BG provide high-quality training @ home or @ class. –- steve.parker@softuni.de."
#
# #sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# #sys.stdin = StringIO(test_input3)

text = input()
pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+\b"

valid_emails = [el.group() for el in re.finditer(pattern,text)]
print("\n".join(valid_emails))
#\s?\w+-?\.?\w+\.?@\w+-?\.?\w+\.?\w+\.?\w+\b