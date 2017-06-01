
import re

pattern = r"\d{3,4}\-\d{5,8}"
print re.match(pattern, "010-12345678") != None

###
s = "a b   c"
print s.split(" ")
print re.split(r"\s+", s)

###

pattern = r"(\d{3,4})\-(\d{5,8})"
m = re.match(pattern, "010-12345678")

print m.group(0)
print m.group(1)
print m.group(2)

