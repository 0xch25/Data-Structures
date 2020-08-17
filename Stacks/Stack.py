'''implementation of Stack [FIFO] using simple Arrays(push,pop,display,top)'''


class Stack:
    def __init__(self):
        self.items = []

    # push to insert an element
    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def display(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def top(self):
        if not self.is_empty():
            return self.items[-1]
    def min_ele(self):
        return min(self.items)


s = Stack()
s.push(5)
s.push(4)
s.push(3)
print(s.min_ele())
print(s.display())
s.pop()
print(s.display())
print(s.top())
print(s.is_empty())
s.pop()
print(s.display())
s.pop()
print(s.is_empty())
