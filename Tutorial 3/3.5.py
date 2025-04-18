import turtle
import math

win = turtle.Screen()
win.bgcolor("white")

hexagon = turtle.Turtle()
hexagon.speed(0)  

def create_hexagon(size, color):
    hexagon.fillcolor(color)
    hexagon.begin_fill()
    for _ in range(6):
        hexagon.forward(size)
        hexagon.left(60)
    hexagon.end_fill()

def create_radial_hex_pattern(num_hexagons, size, color):
    angle = 360 / num_hexagons
    for i in range(num_hexagons):
        create_hexagon(size, color)
        hexagon.left(angle)

create_radial_hex_pattern(10, 50, "blue")

turtle.done()
