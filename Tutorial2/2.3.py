def is_pal(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True

s = input("Enter the string: ")
print("The string is palindrome" if is_pal(s) else "The string is not palindrome")
