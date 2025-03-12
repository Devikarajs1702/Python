def dec_to_bin(n):
    bin_str = ""

    if n == 0:
        return "0"

    while n > 0:
        bin_str = str(n % 2) + bin_str  
        n //= 2
        print(bin_str)

    return bin_str


num = int(input("Enter a decimal number: "))
print(f"Binary representation: {dec_to_bin(num)}")
