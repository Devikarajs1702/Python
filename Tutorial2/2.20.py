num_names = int(input("Enter the number of names: "))

name_list = []
for i in range(num_names):
    name = input(f"Enter name {i+1}: ")
    name_list.append(name)

name_list.sort()

print("\nNames in alphabetical order:")
for name in name_list:
    print(name)
