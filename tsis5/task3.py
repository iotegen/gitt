import re

text = "aa_fas_lkdj faaaf"

pat = r"[a-z]+_[a-z]+"

x = re.findall(pat, text)

print(x)