import re


REGEX = re.compile(r"\w+")


#Whole string match
result = re.fullmatch(REGEX, "Hello 5 you")
print("fullmatch: ", result)

#Partial match
result = re.match(REGEX, "Hello 5 you")
print("match: ", result)


