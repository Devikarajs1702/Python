def reverse_digits(number):
    rev_num = 0
    
    while number > 0:
        digit = number % 10 
        rev_num = rev_num * 10 + digit  
        number //= 10
    
    return rev_num

num_input = int(input("Enter a number: "))

if num_input < 0:
    print(f"Reversed number: -{reverse_digits(abs(num_input))}")
else:
    print(f"Reversed number: {reverse_digits(num_input)}")
