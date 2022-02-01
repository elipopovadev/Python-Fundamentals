symbol1 = input()
symbol2 = input()

def return_characters(symbol1, symbol2):
    symbol1 = ord(symbol1)
    symbol2 = ord(symbol2)
    result = []
    for i in range(symbol1 + 1, symbol2):
        char = chr(i)
        result.append(char)
    result = " ".join(result)
    
    return result

print(return_characters(symbol1, symbol2))
