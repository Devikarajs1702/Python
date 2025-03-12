def fact(n):
    if n in (0, 1):
        return 1
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def comb(n, r):
    if r > n:
        return "r cannot be greater than n"
    return fact(n) // (fact(r) * fact(n - r))

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))
print(f"nCr ({n}C{r}) = {comb(n, r)}")
