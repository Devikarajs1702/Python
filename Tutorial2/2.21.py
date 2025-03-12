num_elements = int(input("Enter the number of elements: "))

even_total = 0

for i in range(num_elements):
    value = int(input(f"Enter number {i+1}: "))
    if value % 2 == 0:
        even_total += value

print(f"\nSum of all even numbers: {even_total}")
