def check_armstrong(n_value):
    temp_value = n_value
    digit_count = 0
    power_sum = 0
    
    num_copy = n_value
    while num_copy > 0:
        num_copy //= 10
        digit_count += 1

    num_copy = temp_value
    while num_copy > 0:
        digit = num_copy % 10
        power_sum += digit ** digit_count
        num_copy //= 10

    return temp_value == power_sum

number = int(input("Enter a number: "))

if check_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is NOT an Armstrong number.")
