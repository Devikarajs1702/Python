def unique_values(lst):
    return list(set(lst))

num_elements = int(input("Enter the number of elements: "))
elements = [int(input(f"Enter number {i+1}: ")) for i in range(num_elements)]

print(f"\nList after removing duplicates: {unique_values(elements)}")
