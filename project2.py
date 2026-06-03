'''
Jacob Nguyen
I made a scene of a boat at sea
I wanted it to be simple and calm
'''

import turtle

def setup():
    t = turtle.Turtle()
    t.speed(0)
    return t, turtle.Screen()

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

def draw_scene(t):
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    # ocean
    go(t, -300, 0)
    rect(t, 600, 200, "royalblue")

    # sun
    go(t, 180, 140)
    circ(t, 30, "yellow")

    # boat
    go(t, -60, 30)
    rect(t, 120, 30, "brown")

    # sail
    go(t, 0, 60)
    tri(t, 70, "white")

    # island
    go(t, 120, 0)
    circ(t, 25, "tan")

    # tree
    go(t, 135, 25)
    rect(t, 10, 40, "brown")
    go(t, 130, 60)
    circ(t, 20, "green")

    # cloud
    go(t, -150, 150)
    circ(t, 15, "white")
    go(t, -130, 160)
    circ(t, 18, "white")

def main():
    t, screen = setup()
    draw_scene(t)
    turtle.done()

if __name__ == "__main__":
    main()