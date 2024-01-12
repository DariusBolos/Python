from functools import reduce


def ex1(subject):
    with open("ex1/text.txt", 'r') as file:
        lines = file.readlines()

        content = list(map(lambda entry: entry.strip().split(','), lines))
        keptEntries = list(filter(lambda entry: subject == entry[1], content))

        grades = list(map(lambda entry: int(entry[2]), keptEntries))
        average = reduce(lambda x, y: x + y, grades) / len(grades)

    print(average)
