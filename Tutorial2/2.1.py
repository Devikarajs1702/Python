def exclude_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

sample_text = "Hello, World!"
print("String after excluding vowels:", exclude_vowels(sample_text))
