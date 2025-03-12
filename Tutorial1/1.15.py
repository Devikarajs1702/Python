def check_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1): 
        if number % divisor == 0:
            return False
    return True

for value in range(2, 1000):
    if check_prime(value):
        print(value, end=" ")
