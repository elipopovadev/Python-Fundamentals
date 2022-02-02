def perfect_number_checker(number):
    all_divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            all_divisors.append(i)
    half_of_sum_divisors = sum(all_divisors) // 2
    if number == half_of_sum_divisors:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")
               
number = int(input())        
perfect_number_checker(number)