import re

section_pattern = re.compile("[a-zA-Z][a-zA-Z][a-zA-Z][0-9][0-9]")
pattern_default = re.compile("[a-zA-Z][a-zA-Z][a-zA-Z][0-9][0-9][a-zA-Z][a-zA-Z][a-zA-Z0-9_][a-zA-Z0-9_][0-9][0-9][0-9][0-9]")

b = ["123", "a", "ab", "ab2"]


print(pattern_default.match("123"))
print(pattern_default.match("a"))
print(pattern_default.match("ab"))
print(pattern_default.match("cbb"))
print(pattern_default.match("1b"))
print(pattern_default.match("BEK31BOMV0301"))


m = pattern_default.match("1b")
if m:
    print("Match m")

n = pattern_default.match("BEK31BOMV0301")

if n:
    print("match n")
