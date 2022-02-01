sequence = input().split(" ")

def sort(sequence):
    sequence_int = list(map(int, sequence))
    sequence_int.sort()
    return sequence_int                 

print(sort(sequence))