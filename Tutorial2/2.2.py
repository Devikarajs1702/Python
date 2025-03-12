text_input = input("Enter the string: ")
output_chars = []
for i in range(len(text_input)):
    if i % 2 == 0:
        output_chars.append(text_input[i])

print("".join(output_chars))
