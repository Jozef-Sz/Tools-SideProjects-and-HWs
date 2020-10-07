import turtle
from math import sin, radians, pi

# 4.3 Exercises

# Exercise 1
# def square(t):
#   for i in range(4):
#     t.fd(30)
#     t.lt(90)

# bob = turtle.Turtle()
# square(bob)


# Exercise 2
# def square(t, length):
#   for i in range(4):
#     t.fd(length)
#     t.lt(90)

# bob = turtle.Turtle()
# square(bob, 45)


# Exercise 3
# def polygon(t, length, n):
#   for i in range(n):
#     t.fd(length)
#     t.lt(360 / n)

# bob = turtle.Turtle()

# polygon(bob, 50, 3)
# bob.clear()
# polygon(bob, 60, 4)
# bob.clear()
# polygon(bob, 45, 5)
# bob.clear()
# polygon(bob, 50, 6)


# Exercise 4
# def polygon(t, n, length):
#   for i in range(n):
#     t.fd(length)
#     t.lt(360 / n)

# My version
# def circle(t, r):
#   if r < 0:
#     print('Warning: radius should be positive number!')
#     r = abs(r)
    
#   circumference = 2 * r * 3.141592
#   approx_length = 10
#   approx_sides = int(circumference / approx_length)
#   current_angle = 360 / approx_sides

#   while (current_angle >= 5) or (current_angle <= 1):
#     if current_angle >= 5:
#       if approx_length - 1 == 0:
#         break
#       approx_length -= 1
#     else:
#       if approx_length + 1 == 0:
#         break
#       approx_length += 1

#     approx_sides = int(circumference / approx_length)
#     current_angle = 360 / approx_sides

#   polygon(t, approx_sides, approx_length)

# Text book version
# def circle(t, r):
#   circumference = 2 * 3.141592 * r
#   n = int(circumference / 3) + 3
#   length = circumference / n
#   polygon(t, n, length)

# bob = turtle.Turtle()

# bob.speed(0)
# circle(bob, 60)
# bob.clear()
# circle(bob, 130)
# bob.clear()
# circle(bob, 10)
# bob.clear()
# circle(bob, -90)
# bob.clear()
# circle(bob, 200)


# Exercise 5
# def polyline(t, n, length, angle):
#   for i in range(n):
#     t.fd(length)
#     t.lt(angle)

# def polygon(t, n, length):
#   angle = 360 / n
#   polyline(t, n, length, angle)

# def arc(t, r, angle):
#   arc_length = 2 * 3.141592 * r * angle / 360
#   n = int(arc_length / 3) + 1
#   step_length = arc_length / n
#   step_angle = angle / n
#   polyline(t, n, step_length, step_angle)

# def circle(t, r):
#   print()
#   arc(t, r, 360)

# bob = turtle.Turtle()

# arc(bob, 120, 90)


# 4.12 Exercises
# Exercise 4.2
def polyline(t, n, length, angle):
  for i in range(n):
    t.fd(length)
    t.lt(angle)

def arc(t, r, angle):
  arc_length = 2 * pi * r * angle / 360
  n = int(arc_length / 3) + 1
  step_length = arc_length / n
  step_angle = angle / n
  polyline(t, n, step_length, step_angle)

def petal(t, r, angle):
  for i in range(2):
    arc(t, r, angle)
    t.lt(180 - angle)

def flower_stem(t, height, angle):
  r =  (height / 2) / sin(radians(angle / 2))
  t.rt(90 + angle / 2)
  arc(t, r, angle)
  t.lt(180 - angle / 2)

# Final function
def flower(t, n_petal, r_petal, angle_petal, height_stem, angle_stem):
  for j in range(n_petal):
    petal(t, r_petal, angle_petal)
    t.lt(360 / n_petal)
  flower_stem(t, height_stem, angle_stem)


bob = turtle.Turtle()

bob.speed(0)
flower(bob, n_petal=5, r_petal=80, angle_petal=45, height_stem=150, angle_stem=40)
turtle.done()