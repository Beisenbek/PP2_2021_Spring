import re

txt = "The rain in Spain 1234"
x = re.search(r"(?P<text>.+)(?P<number>\b[0-9]+)", txt)
print(x)
print(x.groups())
print(x.group(1))
print(x.group(2))
print(x.group("text"))
print(x.group("number"))