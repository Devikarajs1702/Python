def check_prime(num):
    if num < 2:
        return False
    for val in range(2, int(num ** 0.5) + 1):
        if num % val == 0:
            return False
    return True

def categorize_numbers(lst):
    prime_nums = [x for x in lst if check_prime(x)]
    composite_nums = [x for x in lst if x > 1 and not check_prime(x)]
    return prime_nums, composite_nums

num_count = int(input("Enter the number of elements: "))
numbers = [int(input(f"Enter positive integer {i+1}: ")) for i in range(num_count) if int(input(f"Enter positive integer {i+1}: ")) > 0]

primes, composites = categorize_numbers(numbers)

print(f"\nPrime numbers: {primes}")
print(f"Composite numbers: {composites}")
