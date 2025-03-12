def filter_words(text, remove_list):
    words = text.split()
    result_words = [word for word in words if word not in remove_list]
    return " ".join(result_words)

input_text = input("Enter a string: ")
remove_list = input("Enter words to remove (separated by spaces): ").split()

filtered_text = filter_words(input_text, remove_list)
print("\nString after removing given words:")
print(filtered_text)
