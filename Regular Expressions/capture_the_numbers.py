import re

pattern = re.compile("\d+")
text = input()
all_matches = []
while True:
    if len(text) == 0:
        break
    matches = pattern.finditer(text)
    for match in matches:
        all_matches.append(match.group())
    text = input()
    
for element in all_matches:
    print(element, end=" ")
    