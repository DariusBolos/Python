lines = int(input("Number of lines in triangle: "))


def pascals_triangle(nrLines: int):
    print(1, end='\n')
    arr = [1, 1]
    print(*arr, sep=' ')    # printing the first two lines that are generic for every triangle
    for line in range(2, nrLines):
        for index, elem in enumerate(reversed(arr)):    # iterating from the final element of the current array to not lose any values
            if index < line - 1:
                arr[index] += arr[index + 1]  #adding the elements from the previous line, it results the new element of the current line
        arr.insert(0, 1)    # inserting 1 as the first element of the line because every new line starts and symmetrically ends with a 1
        print(*arr, sep=' ')    #printing the remaining lines of the triangle


pascals_triangle(lines)
