from ex2.sortedQueue import SortedQueue


class ReverseSortedQueue(SortedQueue):
    def __init__(self):
        super().__init__()

    def add_number(self, value):
        self.queue.append(value)
        self.queue = sorted(self.queue, reverse=True)

    def to_file(self, filename):
        string = reduce(lambda x: x + '\n', map(str, self.queue))

        with open(filename, 'w') as file:
            file.write(string)
