class SortedQueue(object):
    def __init__(self):
        self.queue = []

    def add_number(self, value):
        self.queue.append(value)
        self.queue = sorted(self.queue)

    def remove_number(self, value):
        self.queue.remove(value)
