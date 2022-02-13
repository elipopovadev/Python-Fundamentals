import re

pattern = re.compile(r"(^|(?<=\s))[a-zA-Z0-9]+[\-_\.]*\w+@\w+[\-_\.]*\w+\.[\w\.]+\b")
text = input()

matches = pattern.finditer(text)
for match in matches:
    print(match.group())
    
    
# valid emails: info@softuni-bulgaria.org,
# kiki@hotmail.co.uk, no-reply@github.com,
# s.peterson@mail.uu.net, info-bg@software-university.software.academy. 

# invalid emails: --123@gmail.com, …@mail.bg,
# .info@info.info, _steve@yahoo.cn, mike@helloworld, mike@.unknown.soft., s.johnson@invalid-.
    