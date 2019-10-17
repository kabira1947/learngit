import re
str = "The rain in Spain pbrazil"
x = re.split("\s", str, 1)
print(x)

x1 = re.sub("\s", "9", str)
print(x1)

x2 = re.split("\s", str, 1)
print(x2)


x3 = re.findall("ai", str)
print(x3)


x4 = re.search(r"\bS\w+", str)
print(x4.span())

x5 = re.search(r"\bS\w+", str)
print(x5.string)

x6 = re.search(r"\bS\w+", str)
print(x6.group())

