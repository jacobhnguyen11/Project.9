'''
Jacob Nguyen

Refactored Project 2 Scene

Improvements Made:
- Broke the large draw_scene() function into smaller helper functions
- Removed redundancy by creating reusable, parameterized functions 
- Organized code and separated positioning from drawing logic.
- Added an enhanced scene with multiple boats, clouds, and islands to demonstrate
  how reusable functions make complex scenes easier to build.
'''

import turtle

# Setup
def setup():
    t = turtle.Turtle()
    t.speed(0)
    return t, turtle.Screen()

# Basic Shapes
def rect(t, w, h, c):
    t.fillcolor(c)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()

def tri(t, s, c):
    t.fillcolor(c)
    t.begin_fill()
    for _ in range(3):
        t.forward(s)
        t.left(120)
    t.end_fill()

def circ(t, r, c):
    t.fillcolor(c)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def go(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Helper Draw Functions
def draw_ocean(t):
    go(t, -300, 0)
    rect(t, 600, 200, "royalblue")

def draw_sun(t, x, y, r=30):
    go(t, x, y)
    circ(t, r, "yellow")

def draw_boat(t, x, y):
    # boat base
    go(t, x, y)
    rect(t, 120, 30, "brown")

    # sail
    go(t, x + 60, y + 30)
    tri(t, 70, "white")

def draw_island(t, x, y):
    go(t, x, y)
    circ(t, 25, "tan")

def draw_tree(t, x, y):
    # trunk
    go(t, x, y)
    rect(t, 10, 40, "brown")

    # leaves
    go(t, x - 5, y + 35)
    circ(t, 20, "green")

def draw_cloud(t, x, y, size=15):
    # cluster of circles
    go(t, x, y)
    circ(t, size, "white")

    go(t, x + size + 5, y + 10)
    circ(t, size + 3, "white")

# Original Scene
def draw_scene(t):
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    draw_ocean(t)
    draw_sun(t, 180, 140)

    draw_boat(t, -60, 30)

    draw_island(t, 120, 0)
    draw_tree(t, 135, 25)

    draw_cloud(t, -150, 150)

# Enhanced Scene
def draw_enhanced_scene(t):
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    draw_ocean(t)
    draw_sun(t, 180, 140)

    # multiple boats
    draw_boat(t, -200, 40)
    draw_boat(t, -60, 30)
    draw_boat(t, 100, 50)

    # multiple islands + trees
    draw_island(t, 120, 0)
    draw_tree(t, 135, 25)

    draw_island(t, -250, 0)
    draw_tree(t, -235, 25)

    # multiple clouds
    draw_cloud(t, -150, 150)
    draw_cloud(t, 0, 160, 20)
    draw_cloud(t, 120, 140, 18)

# Main
def main():
    t, screen = setup()

    # FIRST: original scene (must match Project 2)
    draw_scene(t)

    screen.onclick(lambda x, y: switch_scene(t, screen))

    turtle.done()

def switch_scene(t, screen):
    t.clear()
    draw_enhanced_scene(t)

# ---------------- RUN ----------------
if __name__ == "__main__":
    main()