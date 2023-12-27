from math import gcd


def simplify(a):
    d = gcd(a[0], a[1])
    return a[0] // d, a[1] // d


def add(a, b):
    return simplify((a[0] * b[1] + a[1] * b[0], a[1] * b[1]))


def add_frac(fracs, frac):
    fracs.append(frac)


def sum_frac(fracs):
    sum = 0, 1
    for frac in fracs:
        sum = add(sum, frac)
    return sum


def test_sum_frac():
    assert sum_frac([(1, 2), (2, 3), (1, 2)]) == (20, 12)
    assert sum_frac([(1, 2), (1, 2)]) == (4, 4)


def test_add():
    assert add((1, 2), (2, 3)) == (7, 6)
    assert add((1, 2), (1, 2)) == (4, 4)


def menu():
    return """
    1 - add frac
    2 - sum fracs
    3 - remove frac
    4 - minimum value
    5 - maximum value
    0 - exit
    """


def test_simplify():
    assert simplify((4, 4)) == (1, 1)


def sub(a, b):
    return simplify((a[0] * b[1] - a[1] * b[0], a[1] * b[1]))


def mult(a, b):
    return simplify((a[0] * b[0], a[1] * b[1]))


def div(a, b):
    return simplify((a[0] * b[1], a[1] * b[0]))


def remove_frac(position: int, fracs: list):
    fracs.pop(position)


def get_min_element(fracs: list) -> tuple:
    minimum = fracs[0]
    for frac in fracs:
        if frac < minimum:
            minimum = frac

    return minimum


def get_max_element(fracs: list) -> tuple:
    maximum = fracs[0]
    for frac in fracs:
        if frac > maximum:
            maximum = frac

    return maximum


def main():
    fracs = []
    while True:
        print(menu())
        opt = int(input("option: "))

        if opt == 1:
            n = int(input("n = "))
            m = int(input("m = "))

            add_frac(fracs, (n, m))

        if opt == 2:
            s = sum_frac(fracs)
            print(s)

        if opt == 0:
            break

        if opt == 3:
            pos = int(input('position: '))
            remove_frac(pos, fracs)

        if opt == 4:
            print(get_min_element(fracs))

        if opt == 5:
            print(get_max_element(fracs))


main()
