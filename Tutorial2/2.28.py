def sort_bubble(list):
    size = len(list)
    for i in range(size):
        for j in range(0, size - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

elem_count = int(input("Enter the number of elements: "))
elements = [int(input(f"Enter number {i+1}: ")) for i in range(elem_count)]

sort_bubble(elements)

print(f"\nSorted list in non-decreasing order: {elements}")
