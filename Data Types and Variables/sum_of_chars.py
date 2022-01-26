lines = int(input())
sum = 0
for i in range(lines):
    letter = input()
    sum += ord(letter)
    
print(f'The sum equals: {sum}')
