import turtle


# functions draw in the mentioned direction

def draw_forward():
    turtle.forward(10)
    append_file('auxiliary.txt', 'w')


def draw_backward():
    turtle.backward(10)
    append_file('auxiliary.txt', 's')


def turn_right():
    turtle.right(45)
    append_file('auxiliary.txt', 'd')


def turn_left():
    turtle.left(45)
    append_file('auxiliary.txt', 'a')


def pen_up():
    turtle.penup()
    append_file('auxiliary.txt', 'f')


def pen_down():
    turtle.pendown()
    append_file('auxiliary.txt', 'g')


def exit_canvas():
    turtle.Screen().bye()


def append_file(filename, key):  # appends a pressed key to the file
    with open(filename, 'a') as file:
        file.write(f'{key} ')


def key_events():  # main press event manager
    turtle.onkey(draw_forward, 'w')
    turtle.onkey(draw_backward, 's')
    turtle.onkey(turn_right, 'd')
    turtle.onkey(turn_left, 'a')
    turtle.onkey(pen_up, 'f')
    turtle.onkey(pen_down, 'g')
    turtle.onkey(exit_canvas, 'Return')


def draw_with_key(key):  # manages the pressed keys from the file by calling a specific function using a dictionary
    turtle.TurtleScreen._RUNNING = True
    dict = {
        'w': draw_forward,
        's': draw_backward,
        'd': turn_right,
        'a': turn_left,
        'f': pen_up,
        'g': pen_down
    }

    dict[key]()
