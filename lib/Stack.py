class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return True if self.size() == 0 else False

    def push(self, item):
        if self.size() < self.limit:
            self.items.append(item)

    def pop(self):
        if self.size() > 0:
            return self.items.pop()

    def peek(self):
        if self.size() > 0:
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)

    def full(self):
        return True if self.size() == self.limit else False

    def search(self, target):
        if target not in self.items:
            return -1
        elif target == self.items[-1]:
            return 0
        else:
            return (len(self.items) - 1) - self.items.index(target)
