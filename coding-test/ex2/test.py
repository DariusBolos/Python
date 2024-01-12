from ex2.sortedQueue import SortedQueue
import random


def test_add_removal():
    queueObj = SortedQueue()
    value = random.randint(1, 10000)

    queueObj.add_number(value)
    assert queueObj.queue[0] == value

    queueObj.remove_number(value)
    assert queueObj.queue == []
