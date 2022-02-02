def password_checker(password):
    is_valid = True
    length = len(password)
    if not 6 <= length <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
        
    for symbol in password:
        digit_checker = symbol.isdigit() 
        letter_checher = symbol.isalpha()
        if digit_checker == False and letter_checher == False:
            is_valid = False
            print("Password must consist only of letters and digits")
            break
        
    password = list(password)
    sum_digits = sum(d.isdigit() for d in password)
    if sum_digits < 2:
        is_valid = False
        print("Password must have at least 2 digits")
    
    if is_valid == True:
        print("Password is valid")
        

password = input()
password_checker(password)