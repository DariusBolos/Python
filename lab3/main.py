import turtle


def draw_rectangle(pen, length, width):  # draws a rectangle with the specified dimensions on the screen
    is_length = True
    for ind in range(4):
        if is_length:
            pen.forward(length)
            pen.left(90)
            is_length = False
        else:
            pen.forward(width)
            pen.left(90)
            is_length = True


def draw_curve(pen):  # draws a curve on the screen
    for i in range(0, 200, 5):
        pen.right(5)
        pen.forward(5)


def draw_triangle(pen, length):  # draws a triangle on the screen
    for ind in range(3):
        pen.forward(length)
        pen.left(120)


def set_pen(pen, x_point, y_point):  # sets the location on the pen on screen
    pen.up()
    pen.goto(x_point, y_point)
    pen.down()


def function1(pen):
    draw_rectangle(pen, 200, 100)
    set_pen(pen, 50, 50)
    draw_rectangle(pen, 50, 25)


def function2(pen):
    pen.left(140)  # drawing the left line
    pen.forward(113)
    draw_curve(pen)  # drawing the left curve
    pen.left(120)
    draw_curve(pen)  # drawing the right curve
    pen.forward(112)  # drawing the right line


def function3(pen):  # draws the two houses one piece at the time using the defined functions
    pen2 = turtle.Turtle()
    pen2.width(3)

    set_pen(pen, 100, 0)
    draw_rectangle(pen, 200, 200)
    set_pen(pen2, -100, 0)
    draw_rectangle(pen2, -200, 200)

    set_pen(pen, 100, 200)
    draw_triangle(pen, 200)
    set_pen(pen2, -300, 200)
    draw_triangle(pen2, 200)

    set_pen(pen, 180, 0)
    draw_rectangle(pen, 50, 80)
    set_pen(pen2, -180, 0)
    draw_rectangle(pen2, -50, 80)

    set_pen(pen, 120, 110)
    draw_rectangle(pen, 60, 60)
    set_pen(pen2, -120, 110)
    draw_rectangle(pen2, -60, 60)

    set_pen(pen, 220, 110)
    draw_rectangle(pen, 60, 60)
    set_pen(pen2, -220, 110)
    draw_rectangle(pen2, -60, 60)

    pen2.reset()
    pen2.hideturtle()


def main():
    t = turtle.Turtle()
    turtle.Screen().screensize(600, 800)
    while True:
        t.width(3)
        value = int(input("""
                1 - rectangles
                2 - heart
                3 - houses
                0 - exit
            """))

        if value == 0:
            break
        else:
            dict = {
                1: function1,
                2: function2,
                3: function3
            }

            dict[value](t)
            t.reset()
            t.hideturtle()


main()
