
class Stack:

    def __init__(self):
        self.last = []

    def get_list(self):
        ans = self.last[::-1]
        print(ans)

    def is_empty(self):
        if self.last:
            print('Is Not Empty')
        else:
            print('Is Empty')

    def push(self, value):
        self.last.append(value)
        self.get_list()

    def pop(self):
        ans = self.last.pop()
        self.get_list()


stack = Stack()
stack.is_empty()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
