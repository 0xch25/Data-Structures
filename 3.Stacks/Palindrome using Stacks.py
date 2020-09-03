'''Program to check weather the given string is palindrome or not'''
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


s = Stack()
str= input("enter the string:")

for char in str:
    s.push(char)

str2=""
while not s.is_empty():
    str2 = str2 + s.pop()

if str == str2:
    print('The string is a palindrome')
else:
    print('The string is not a palindrome')