from collections import Counter

def rmv_all_dupes(lst):
    freq = Counter(lst)
    return [x for x in lst if freq[x] == 1]

n = int(input("Enter the number of elements: "))
nums = [int(input(f"Enter number {i+1}: ")) for i in range(n)]

print(f"\nList after completely removing duplicates: {rmv_all_dupes(nums)}")
