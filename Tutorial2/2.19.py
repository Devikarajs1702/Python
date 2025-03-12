def fib(num):
    if num <= 0:
        return "Invalid input. Please enter a positive integer."
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

pos = int(input("Enter the position (n) to find the Fibonacci number: "))
print(f"The {pos}th Fibonacci number is: {fib(pos)}")
