def is_even(num):
    print(f"{num} is Even" if num % 2 == 0 else f"{num} is Odd")

def num_type(num):
    if num > 0:
        print(f"{num} is Positive")
    elif num < 0:
        print(f"{num} is Negative")
    else:
        print(f"{num} is Zero")

def factors(num):
    print(f"Factors of {num}: ", end="")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print()

while True:
    print("\nMenu:")
    print("1. Check Even or Odd")
    print("2. Check if Number is Positive, Negative, or Zero")
    print("3. Generate Factors of a Number")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice in (1, 2, 3):
        num = int(input("Enter a number: "))

    if choice == 1:
        is_even(num)
    elif choice == 2:
        num_type(num)
    elif choice == 3:
        factors(num)
    elif choice == 4:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Enter a valid option (1-4).")
