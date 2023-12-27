from module1.alphabet import al
from module1.keys import key_events, draw_with_key, exit_canvas
import turtle


def draw_word():  # draws the word given by the user
    turtle.TurtleScreen._RUNNING = True
    word = input("Enter a word to be drawn: ")
    for letter in word:
        al[letter](turtle)


def manual_draw():  # enables manual drawing
    turtle.TurtleScreen._RUNNING = True
    clear_auxiliary()
    key_events()
    turtle.listen()
    turtle.done()


def clear_auxiliary():  # clears auxiliary file used to potentially store data in the main output file
    with open('auxiliary.txt', 'w') as file_clear:
        file_clear.write('')


def save_to_file():  # saves pressed keys to an output file
    with open('auxiliary.txt', 'r') as file_read:
        string = file_read.read()
        with open('output.txt', 'w') as file_write:
            file_write.write(string)


def read_keys():  # gets the keys from the output file
    keys = []
    with open('output.txt', 'r') as file:
        string = file.read()
        keys = string.split()

    return keys


def draw_keys():  # draws using the read pressed keys from the output
    keys = read_keys()
    for key in keys:
        draw_with_key(key)

    turtle.listen()
    turtle.onkey(exit_canvas, 'Return')
    turtle.done()