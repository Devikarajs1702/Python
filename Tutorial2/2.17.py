import math

def fact(num):
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res

def sine_series(x, terms):
    sine_val = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / fact(2 * n + 1)
        sine_val += term
    return sine_val

x_deg = float(input("Enter the value of x in degrees: "))
n_terms = int(input("Enter the number of terms: "))

x_rad = math.radians(x_deg)
result = sine_series(x_rad, n_terms)

print(f"sin({x_deg}) ≈ {result}")
