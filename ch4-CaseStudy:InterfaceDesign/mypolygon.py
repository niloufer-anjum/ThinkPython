from swampy.TurtleWorld import *
import math

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, length, n):
    polyline(t, n, length, 360.0/n)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length/3)+1
    step_length = arc_length/n
    step_angle = float(angle)/n
    polyline(t, n, step_length, step_angle)

def square(t, length):
    polygon(t, length, 4)

def circle(t, r):
    arc(t, r, 360)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

square(bob, 100)
polygon(bob, 100, 8)
circle(bob, 100)
arc(bob, 100, 90)

wait_for_user()
