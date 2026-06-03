"""
Jacob Nguyen
Project1 CS110 S26
"""

from turtle import *

# setup screen
bgcolor("skyblue")
hideturtle()
speed(0)

# draw sun
sun_x = 100
sun_y = 125
sun_radius = 50
ray_length = 80
num_rays = 12

penup()
goto(sun_x, sun_y)
pendown()
color("yellow")
begin_fill()
circle(sun_radius)
end_fill()

# sun rays
penup()
goto(sun_x, sun_y + sun_radius)  # start at top of sun
pendown()
for i in range(num_rays):
    forward(ray_length)
    backward(ray_length)
    right(360 / num_rays)

# draw grass
penup()
goto(-300, -100)
pendown()
color("green")
begin_fill()
for _ in range(2):
    forward(600)
    right(90)
    forward(200)
    right(90)
end_fill()

# draw a tree
tree_x = -150
tree_y = -100
tree_height = 100

# trunk
penup()
goto(tree_x, tree_y)
pendown()
color("brown")
begin_fill()
for _ in range(2):
    forward(20)
    left(90)
    forward(tree_height)
    left(90)
end_fill()
# leaves
penup()
goto(tree_x + 10, tree_y + tree_height)
pendown()
color("darkgreen")
begin_fill()
circle(40)
end_fill()

# draw flowers
num_flowers = 5
start_x = -250

for i in range(num_flowers):
    penup()
    goto(start_x + i * 80, -100)
    pendown()
    # alternate colors for fun
    if i % 2 == 0:
        color("pink")
    else:
        color("red")
    begin_fill()
    circle(10)
    end_fill()

done()