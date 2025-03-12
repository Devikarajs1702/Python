def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

num_input = int(input("Enter a number: "))

if num_input < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num_input} is {fact(num_input)}")
