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


# Mini Projekt
def polyline(t, n, length, angle):
  for _ in range(n):
    t.fd(length)
    t.lt(angle)


def arc(t, r, angle):
  arc_length = 2 * pi * r * angle / 360
  n = int(arc_length / 3) + 1
  step_length = arc_length / n
  step_angle = angle / n
  polyline(t, n, step_length, step_angle)


def petal(t, r, angle):
  """
  Draws a petal using two arcs.
  
  t:     Turtle
  r:     radius of the arcs
  angle: angle (degrees) that subtends the arcs
  """
  for _ in range(2):
    arc(t, r, angle)
    t.lt(180 - angle)


def perpendicular_arc(t, height, angle):
  """
  Draw an arc with it's end points aligned on top of each other, perpedicular to ground.

  t:      an instance of Turtle()
  height: distance between the ends of the arc
  angle:  sets the depth of the curve
  """
  r =  (height / 2) / sin(radians(angle / 2))
  arc(t, r, angle)


def flower_stem(t, height, angle):
  """
  Draws a stem based on a height and an angle value.

  t:      an instance of Turtle()
  height: height of the stem from the center of flower, to the bottom of the stem
  angle:  angle of the curve in stem
  """
  t.rt(90 + angle / 2)
  perpendicular_arc(t, height, angle)
  t.lt(180 - angle / 2)


def flower_leafs(t, length, width, angle_ground):
  """
  Draws two mirrored leafs with a particular length, width and an angle from ground.

  t:            an instance of Turtle()
  length:       length of leafs from the begining, to the tip
  width:        width of leafs
  angle_ground: relative angle of leafs from the ground
  """
  t.lt(90 - angle_ground - width / 2)
  for _ in range(2):
    perpendicular_arc(t, length, width)
    t.lt(180 - width)

  t.rt(180 - 2 * angle_ground)
  for _ in range(2):
    perpendicular_arc(t, length, width)
    t.lt(180 - width)

  t.lt(-angle_ground + width / 2)


def move(t, x, y=0):
  """
  Moves an instance of Turtle() by a x and y value relative to it's current position.

  t: an instance of Turtle()
  x: distance on x axis
  y: distance on y axis
  """
  current_pos = t.pos()
  t.pu()
  t.setpos(current_pos[0] + x, current_pos[1] + y)
  t.pd()


def flower(t, n_petal, r_petal, angle_petal, height_stem, angle_stem, length_leaf, width_leaf, angle_ground):
  """
  Draws a complete flower with a stem and leafs.
  
  t:            an instance of Turtle()
  n_petal:      number of petals of the flower
  r_petal:      radius of half petal
  angle_petal:  angle of the half petal arc
  height_stem:  height of the stem from the center of flower, to the bottom of the stem
  angle_stem:   angle of the curve in stem
  length_leaf:  length of leafs from the begining, to the tip
  width_leaf:   width of leafs
  angle_ground: relative angle of leafs from the ground
  """
  for _ in range(n_petal):
    petal(t, r_petal, angle_petal)
    t.lt(360 / n_petal)
  flower_stem(t, height_stem, angle_stem)
  flower_leafs(t, length_leaf, width_leaf, angle_ground)
  move(t, 0, height_stem)


# Create turtle instance 
bob = turtle.Turtle()

# Initial settings
# bob.speed(0)
bob._tracer(0)
move(bob, -200)

# Drawing flowers
flower(
  bob, 
  n_petal=7, 
  r_petal=80, 
  angle_petal=55, 
  height_stem=150, 
  angle_stem=95, 
  length_leaf=50, 
  width_leaf=80, 
  angle_ground=0
)

move(bob, 200)
flower(
  bob, 
  n_petal=10, 
  r_petal=50, 
  angle_petal=85, 
  height_stem=300, 
  angle_stem=20, 
  length_leaf=150, 
  width_leaf=10, 
  angle_ground=75
)

move(bob, 200)
flower(
  bob, 
  n_petal=20, 
  r_petal=300, 
  angle_petal=10, 
  height_stem=165, 
  angle_stem=65, 
  length_leaf=150, 
  width_leaf=120, 
  angle_ground=45
)



turtle.done()