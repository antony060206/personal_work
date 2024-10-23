
class StackUsingQuese:
    def __init__(self):
        self.queue = Queue()

    def push(self, element):
        self.queue.enqueue(element)

        for x in range(self.size() - 1):
            self.queue.enqueue(self.queue.pop())

    def pop(self):
        return self.queue.pop()

    def top(self):
        return self.queue.items[self.size() - 1]

    def is_empty(self):
        if(self.size()== 0):
            return True
        else:
            return False

    def size(self):
        i = 0
        for x in (self.queue.items):
            i += 1
        return i

    def __repr__(self):
        return f"StackUsingQueue({self.queue.items[::-1]})"

#The below code only helps to visually represent the Queue class
class Queue:
    def __init__(self):
        self.items = []

    def top(self):
        return self.items[-1]

    def enqueue(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop()



stack = StackUsingQuese()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.top())
print(stack.pop())
print(stack.pop())
stack.push(4)
print(stack.pop())
print(stack.is_empty())
print(stack)