from collections import Counter

def compute_mode(values):
    frequency = Counter(values)
    highest_freq = max(frequency.values())
    mode_values = [num for num, count in frequency.items() if count == highest_freq]
    return mode_values

num_elements = int(input("Enter the number of elements: "))
elements = [int(input(f"Enter number {i+1}: ")) for i in range(num_elements)]

print(f"\nThe mode is: {compute_mode(elements)}")
