def read_file(filename):  # reads content from a file
    with open(filename, 'r') as f:
        file = f.read()
        return file


def clear_file(filename):  # clears the content on a file
    with open(filename, 'w') as f:
        f.write('')


def append_to_file(filename, word):  # appends a new word to the newly written file
    with open(filename, 'a') as f:
        f.write(word)


def replace_words(filename, words_list, to_be_replaced, replacement):
    count = 0       # replaces the by the user given words with the new word
    clear_file(filename)
    for word in words_list:
        if word.rstrip(',.-') == to_be_replaced:
            word = word.replace(to_be_replaced, replacement)
            count += 1
        append_to_file(filename, word)
        append_to_file(filename, ' ')
    return count
