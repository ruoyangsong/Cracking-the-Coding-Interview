class MyQueue(object):
    def __init__(self):
        self.stack = []
    
    def peek(self):
        values = ""
        for i in self.stack:
            values += str(i)
            values += " "
        print(values)
    def pop(self):
        self.stack.pop(0)
        
    def put(self, value):
        self.stack.append(value)

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
        queue.peek()