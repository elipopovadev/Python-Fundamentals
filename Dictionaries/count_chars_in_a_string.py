text = input()
my_dict = {}
for letter in text:
    if letter == " ":
        continue
    if not letter in my_dict:
        my_dict[letter] = 1
    else:
        my_dict[letter] += 1

for (key, value) in my_dict.items():
    print(f"{key} -> {value}")
    