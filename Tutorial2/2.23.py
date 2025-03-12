def calculate_median(values):
    values.sort()
    size = len(values)
    
    if size % 2 == 1:
        return values[size // 2]
    else:
        mid1, mid2 = values[size // 2 - 1], values[size // 2]
        return (mid1 + mid2) / 2

num_elements = int(input("Enter the number of elements: "))

elements = []
for i in range(num_elements):
    value = float(input(f"Enter number {i+1}: "))
    elements.append(value)

median_value = calculate_median(elements)
print(f"\nThe median is: {median_value}")
