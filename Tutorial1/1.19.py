n_values = int(input("Enter the number of elements: "))

even_total = 0
odd_total = 0

for _ in range(n_values):
    value = int(input("Enter a number: "))
    if value % 2 == 0:
        even_total += 1
    else:
        odd_total += 1

print(f"Even numbers: {even_total}")
print(f"Odd numbers: {odd_total}")
