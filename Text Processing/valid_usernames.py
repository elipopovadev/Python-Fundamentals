words = input().split(', ')
valid_words = []

for word in words:
    char_is_valid = False
    for char in word:
        if char.isalpha() or char.isdigit() or char == '-' or char == '_' :
            char_is_valid = True
        else:
            char_is_valid = False
            break
    if char_is_valid and 3 < len(word) < 16:
        valid_words.append(word)

for word in valid_words:
    print (word)
    