n_value = int(input("Enter the value of n: "))

for num in range(1, n_value + 1):
    print(f"\nMultiplication Table of {num}:") 
    for multiplier in range(1, 11):  
        print(f"{num} x {multiplier} = {num * multiplier}")  
