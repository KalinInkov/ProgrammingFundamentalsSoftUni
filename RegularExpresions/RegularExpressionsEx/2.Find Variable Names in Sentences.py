import re
text = input()
pattern = r"(^_|(?<=\s_))[a-zA-Z0-9]+\b"

valid_names = [matched_obj.group() for matched_obj in    re.finditer(pattern,text)]



print(*valid_names,sep=",")