from typing import Union

class Stack:
    def __init__(self):
        self.stack = [1, 2, 'q', 'w', 'e', 3, 4, 'r', 't', 5, 6, 'y', 7]

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def get_from_stack(self,e):
        new = []
        for i in range(len(self.stack)):
            new.append(self.pop())

        for i in range(len(new)):
            self.push(new.pop())
            try:
                if e in self.stack:
                    print(f'Element "{e}" in stack!')
                    self.pop()
            except ValueError:
                return'Element "{e}" not in stack!'
        return self.stack


if __name__ == '__main__':

    s = Stack()
    print(s.get_from_stack(2))
    print(s.get_from_stack(4))
    print(s.get_from_stack(3))
    print(s.get_from_stack(1))
    print(s.get_from_stack(5))
    print(s.get_from_stack(6))
    print(s.get_from_stack(7))
