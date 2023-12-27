def read_matrix(filename):
    matrix = []
    with (open(filename, 'r') as file):
        line = file.readline()
        while line:
            matrixLine = line.split(',')
            elements = []
            for ind in range(len(matrixLine)):
                elements.append(int(matrixLine[ind]))
            matrix.append(elements)
            line = file.readline()

    return matrix


def get_nr_of_zeros(matrix):
    counter = 0
    for ind1 in range(len(matrix)):
        for ind2 in range(len(matrix[ind1])):
            if matrix[ind1][ind2] == 0:
                counter += 1

    return counter


def is_sparse(matrix):
    nrOfZeros = get_nr_of_zeros(matrix)
    nrOfElements = len(matrix) ** 2

    return get_70_percent(nrOfElements) < nrOfZeros


def is_square(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Find the boundaries of the square
    min_row, min_col, max_row, max_col = rows, cols, 0, 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                min_row = min(min_row, i)
                min_col = min(min_col, j)
                max_row = max(max_row, i)
                max_col = max(max_col, j)

    return (min_row, max_row) == (min_col, max_col)


def get_70_percent(nrOfElements):
    return 70 * nrOfElements / 100


def main():
    matrix = read_matrix('input.txt')
    print(is_square(matrix))

main()
