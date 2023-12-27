def sum_diag(matrix):
    result = []

    for i in range(len(matrix)):
        sum_line = 0

        for j in range(len(matrix[i])):
            if i != j:
                sum_line += matrix[i][j]

        result.append(sum_line == matrix[i][i])

    return result


def longest_word(filename):
    f = open(filename, 'r')
    result = []

    for line in f:
        words = line.split(' ')
        max_length = 0
        max_word = ''

        for word in words:
            if len(word.strip()) > max_length:
                max_length, max_word = len(word.strip()), word.strip()

        result.append((max_length, max_word))

    f.close()
    return result


def sum_on_line(column, matrix):
    sum = 0
    for ind in range(len(matrix[column])):
        sum += matrix[ind][column]

    return sum


def perfect_number(number):
    sum_div = 1
    root = int((number ** 0.5) + 1)
    for div in range(2, root):
        if div == root:
            sum_div += div
        else:
            if number % div == 0:
                sum_div += (div + number // div)

    if number == sum_div:
        return True

    return False


def sum_perfect_number(matrix):
    for index in range(len(matrix)):
        sum = sum_on_line(index, matrix)

        if not perfect_number(sum):
            return False

    return True


def count_pali(filename):
    f = open(filename, 'r')
    result = {}

    for line in f:
        words = line.split(' ')

        for word in words:
            word = word.strip()

            if word == word[::-1]:
                if word in result:
                    result[word] += 1
                else:
                    result[word] = 1

    f.close()
    return result


def ascending_sequence(matrix):
    desc_order = False
    for i in range(len(matrix)):
        if desc_order:
            desc_order = False
            matrix[i] = matrix[i][::-1]
        else:
            desc_order = True
        for j in range(1, len(matrix[i])):
            if matrix[i][j - 1] > matrix[i][j]:
                return False

    return True


def write_palindromes(input, output):
    results = []
    with open(output, 'w') as o:
        o.write('')

    with open(input, 'r') as f:
        for line in f:
            numbers = line.split(' ')

            for number in numbers:
                number = number.strip()
                if number == number[::-1]:
                    with open(output, 'a') as o:
                        results.append(int(number))
                        o.write(number + ' ')

    return results


def test_write_palindromes():
    assert write_palindromes('test3.input', 'test3.output') == [121, 222, 8998, 888]


def test_ascending_sequence():
    assert ascending_sequence([
        [1, 2, 3],
        [6, 5, 4],
        [7, 8, 9]
    ])
    assert not ascending_sequence([
        [4, 5, 6],
        [1, 2, 3],
        [7, 8, 9]
    ])


def test_count_pali():
    assert count_pali('test2.input') == {'anna': 2, 'abba': 2}


def test_longest_word():
    assert longest_word('test.input') == [(4, 'mere'), (5, 'totul')]


def test_perfect_number():
    assert perfect_number(6)
    assert not perfect_number(7)


def test_sum_perfect_number():
    assert sum_perfect_number([
        [4, 3, 10],
        [1, 2, 10],
        [1, 1, 8]
    ])


def test_sum_diag():
    assert sum_diag([
        [4, 3, 1],
        [1, 2, 1],
        [0, 5, 1]
    ]) == [True, True, False]


def main():
    pass


test_count_pali()
test_longest_word()
test_sum_diag()
test_perfect_number()
test_sum_perfect_number()
test_ascending_sequence()
test_write_palindromes()
main()
