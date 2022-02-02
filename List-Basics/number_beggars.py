text = input().split(", ")
coins = list(map(int, text))
number_beggars = int(input())
list_output = [0] * number_beggars

for i in range(0, len(coins)):
    currentBeggar = i % number_beggars
    list_output[currentBeggar] += coins[i]

print(list_output)
