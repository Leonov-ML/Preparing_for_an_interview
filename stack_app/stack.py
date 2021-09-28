class Stack:

    def __init__(self):
        self.data = []

    def isEmpty(self):
        return not self.data or False

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return None if self.isEmpty() else self.data.pop()

    def peek(self):
        return None if self.isEmpty() else self.data[-1]

    def size(self):
        return len(self.data)
