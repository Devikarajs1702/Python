import math

def circle_area(r):
    if r < 0:
        return "Radius cannot be negative"
    
    return math.pi * r ** 2

radius = float(input("Enter the radius of the circle: "))
print(f"Area of the circle: {circle_area(radius):.2f}")
