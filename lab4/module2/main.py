from module2.output import show_message
from module2.input import read_words


def main():  # default main function
    word1, word2 = read_words()
    show_message(word1, word2)


main()
