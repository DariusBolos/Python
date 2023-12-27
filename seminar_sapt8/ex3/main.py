# def do_stuff(s1): - falsely written
#     arr = [0] * len(s1) // minus one is not needed correct: len(s1)
#
#     for i in range(len(s1)):
#         w = 2
#         while w < s1[i] and s1[i] % w:
#             w *= 2                        // the smallest power of two bigger than each odd number
#                                           // or the even number itself
#
#         arr[i] = w
#
#     for i in arr:  // i is element not index correct: range(len(arr))
#         arr[i] = arr[i] <= s1[i]
#
#     return arr

#     // return an array with True on the indexes of the even number in the initial array,
#     // values of False otherwise


def do_stuff(s1):
    arr = [0] * (len(s1))

    for i in range(len(s1)):
        w = 2
        while w < s1[i] and s1[i] % w:
            w *= 2

        arr[i] = w

    for i in range(len(arr)):
        arr[i] = arr[i] <= s1[i]

    return arr


def main():
    print(do_stuff([1, 23, 3, 4, 64]))


main()
