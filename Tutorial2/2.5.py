txt = input("Enter the string: ")
chars = list(txt)
odd = []
even = []

for i in range(len(chars)):
    if i % 2 == 0:
        even.append(chars[i])
    else:
        odd.append(chars[i])

print(chars)
print("Even elements:", even)
print("Odd elements:", odd)
