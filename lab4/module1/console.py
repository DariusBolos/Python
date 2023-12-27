from module1.draw import draw_word, manual_draw, save_to_file, draw_keys


def menu():  # menu operating function
    while True:
        value = int(input("""
                1 - draw a word
                2 - manually draw a word
                3 - save pressed keys to file
                4 - draw pressed keys from file
                0 - exit
            """))

        if value == 0:
            break
        else:
            options = {
                1: draw_word,
                2: manual_draw,
                3: save_to_file,
                4: draw_keys
            }

            options[value]()
