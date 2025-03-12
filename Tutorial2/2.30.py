def rmv_dupes(lst):
    uniq_lst = []
    for itm in lst:
        if itm not in uniq_lst:
            uniq_lst.append(itm)
    return uniq_lst

n = int(input("Enter the number of elements: "))
nums = [int(input(f"Enter number {i+1}: ")) for i in range(n)]

print(f"\nList after removing duplicates: {rmv_dupes(nums)}")
