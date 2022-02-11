import re

text = input()
word = input()

pattern = fr"(?i)\b{word}\b"
matches = re.findall(pattern, text)
print(len(matches))
