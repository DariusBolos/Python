from module2.filework import read_file, replace_words


def show_message(to_be_replaced, replacement):            # shows a message in case a word has been replaced or
    filename = 'D:/Coding/Python/lab4/module2/file.txt'   # a default message in case no changes were made
    text = read_file(filename)
    words = text.split()

    counter = replace_words(filename, words, to_be_replaced, replacement)
    if counter:
        print(f'The given word has been replaced {counter} times')
    else:
        print('No changes were made to the file')
