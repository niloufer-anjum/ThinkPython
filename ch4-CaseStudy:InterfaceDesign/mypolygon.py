import turtle
import math

bob = turtle.Turtle()

def square(t, length):
    polygon(t, length, 4)

def polygon(t, length, n):
    polyline(t, length, 360.0, n)

def circle(t, radius):
    arc(t, radius, 360)

def arc(t, radius, angle):
    circumference = 2 * math.pi * radius
    arc_length = circumference/(360.0/angle)
    n = int(arc_length/3)
    polyline(t, 3, angle, n)

def polyline(t, length, angle, n):
    for i in range(n):
        t.fd(length)
        t.lt(angle/n)

square(bob, 200)
polygon(bob, 150, 5)
circle(bob, 150)
arc(bob, 150, 90)
turtle.mainloop()
