def min_max_sum_function(sequence):
    sequence_int = list(map(int, sequence))
    min_value = min(sequence_int)
    max_value = max(sequence_int)
    sum_value = sum(sequence_int)
    print (f"The minimum number is {min_value}")
    print(f"The maximum number is {max_value}")
    print(f"The sum number is: {sum_value}")
    
    
sequence = input().split(" ")   
min_max_sum_function(sequence)
    