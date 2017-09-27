class MyQueue(object):
    def __init__(self):
        self.elements = []

    def peek(self):
        if len(self.elements) > 0:
            return self.elements[0]
        else:
            return None
    def pop(self):
        if len(self.elements) > 0:
            return self.elements.pop(0)
        else:
            return None

    def put(self, value):
        self.elements.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
