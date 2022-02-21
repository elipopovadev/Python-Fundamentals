text = input()
result = ""
bomb_power = 0

for i in range(len(text)):
    if text[i] == ">":
        bomb_power += int(text[i + 1])
        result += text[i]
    elif text[i] != ">" and bomb_power > 0:
        bomb_power -= 1
    else:
        result += text[i]

print(result)
