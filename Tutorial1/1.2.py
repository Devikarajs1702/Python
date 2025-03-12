from math import pi

def circle_area_perimeter(radius):
    area = pi * radius**2
    perimeter = 2 * pi * radius
    return f"Area: {area:.2f} & Perimeter: {perimeter:.2f}"

radius = float(input("Enter the radius of the circle: "))
result = circle_area_perimeter(radius)
print(result)
