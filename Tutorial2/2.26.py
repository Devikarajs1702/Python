def classify_elements(lst):
    int_list = [x for x in lst if isinstance(x, int) and not isinstance(x, bool)]
    float_list = [x for x in lst if isinstance(x, float)]
    str_list = [x for x in lst if isinstance(x, str)]
    return int_list, float_list, str_list

num_items = int(input("Enter the number of elements: "))
data_list = [eval(input(f"Enter element {i+1}: ")) for i in range(num_items)]

integers, floats, strings = classify_elements(data_list)

print(f"\nIntegers: {integers}")
print(f"Floats: {floats}")
print(f"Strings: {strings}")
