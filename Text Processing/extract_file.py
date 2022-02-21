words = input().split('\\')
last_words = words[-1].split('.')

print(f'File name: {last_words[0]}')
print(f'File extension: {last_words[1]}')
