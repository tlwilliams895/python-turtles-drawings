import turtle


def init_objects():
    t = turtle.Turtle()
    t.speed(0)
    return (t, t.getscreen())


def move_turtle(t, x, y):
    t.up()
    t.goto(x, y)
    t.down()


def draw_reg_poly(t, n, s):
    a = int(360/n)
    for i in range(n):
        t.forward(s)
        t.left(a)


def draw_square(t, s):
    draw_reg_poly(t, 4, s)


def draw_triangle(t, s):
    draw_reg_poly(t, 3, s)


def draw_inv_triangle(t, s):
    for i in range(3):
        t.forward(s)
        t.right(120)
