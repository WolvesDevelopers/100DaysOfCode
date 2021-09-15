class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def str(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def isEmpty(self):
        return (self.elements == [])


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def isEmpty(self):
        return (self.length == 0)

    def insert(self, data):
        node = Node(data)
        node.next = None
        if self.length == 0:
            self.head = self.last = node
        else:
            last = self.last
            last.next = node
        self.length = self.length + 1

    def remove(self):
        data = self.head.data
        self.head = self.head.next
        self.length = self.length - 1
        if self.length == 0:
            self.last = None
        return data


class QueuePriority:
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []

    def insert(self, element):
        self.elements.append(element)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.elements)):
            if self.elements[i] > self.elements[maxi]:
                maxi = i
        element = self.elements[maxi]
        self.elements[maxi:maxi+1] = []
        return element


if __name__ == '__main__':

    my_queue = QueuePriority()

    my_queue.insert(1)
    my_queue.insert(3)
    my_queue.insert(55)

    while not my_queue.isEmpty():
        print(my_queue.remove())
