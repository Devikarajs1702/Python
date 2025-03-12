txt = input("Enter the string: ")
for ch in txt:
    if ch == " ":
        txt = txt.replace(" ", "*")

txt += "$"

print(txt)
