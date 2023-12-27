def search_list(list, dict):
    for element in list:
        if element in dict:
            dict[element] += 1
        else:
            dict[element] = 1

    return dict


def common_values(list):
    newList = []
    dict = {}
    count = len(list)
    for element in list:
        dict = search_list(element, dict)

    for value in dict.keys():
        if dict[value] == count:
            newList.append(value)

    return newList


def main():
    list = [[1, 2, 3, 4], [4, 5, 1], [7, 8, 5, 1, 4]]
    print(common_values(list))


main()
