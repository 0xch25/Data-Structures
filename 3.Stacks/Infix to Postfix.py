"""
Implementation of Infix to postfix conversion

"""


class Stack:
    def __init__(self):
        self.items = []
        self.length = 0

    def push(self, val):
        self.items.append(val)
        self.length += 1

    def pop(self):
        if self.empty():
            return None
        self.length -= 1
        return self.items.pop()

    def size(self):
        return self.length

    def peek(self):
        if self.empty():
            return None
        return self.items[0]

    def empty(self):
        return self.length == 0

    def __str__(self):
        return str(self.items)


precedence = {}
precedence['*'] = 3
precedence['/'] = 3
precedence['+'] = 2
precedence['-'] = 2
precedence['('] = 1


def convert(expression):
    print(__convert(expression.split()))


def __convert(tokens):
    postfix = []
    s = Stack()

    for token in tokens:
        if token.isidentifier():
            postfix.append(token)
        elif token == '(':
            s.push(token)
        elif token == ')':
            while True:
                temp = s.pop()
                if temp is None or temp == '(':
                    break
                elif not temp.isidentifier():
                    postfix.append(temp)

        else:  # must be operator
            if not s.empty():
                temp = s.peek()

                while not s.empty() and precedence[temp] >= precedence[token] and token.isidentifier():
                    postfix.append(s.pop())
                    temp = s.peek()

            s.push(token)

    while not s.empty():
        postfix.append(s.pop())

    return postfix


convert("A + B")
convert("A + B * C")
convert("A * ( B + C ) + D")
