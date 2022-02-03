sequence_One = input().split(", ")
sequence_Two = input().split(", ")

result = [substr for substr in sequence_One for text in sequence_Two if substr in text]
print(sorted(set(result), key = result.index))
