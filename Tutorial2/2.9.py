txt = input("Enter the string: ")

length = len(txt)
midpoint = length // 2

for i in range(midpoint - 1, -1, -1):
    print(txt[i], end="")
for i in range(length - 1, midpoint - 1, -1):
    print(txt[i], end="")
