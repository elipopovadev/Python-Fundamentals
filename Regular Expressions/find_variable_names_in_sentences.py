import re

pattern = re.compile(r"(?<!_.)(?<=_)([a-zA-Z\d]+\b)")
text = input()
matches = pattern.findall(text)
print(",".join(map(str, matches)))
