txt = input("Enter the string: ")
subtxt = input("Enter the substring: ")

if subtxt in txt:
    txt = txt.replace(subtxt, "")
    print(txt)
