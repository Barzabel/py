class Node:
    def __init__(self,val):
        self.value = val
        self.prev = None

class Stack:
    def __init__(self):
        self.stack = None
        self.count = 0

    def size(self):
        return self.count

    def pop(self):
        if self.size()== 0:
            return None # если стек пустой
        res  = self.stack.value
        self.stack = self.stack.prev
        self.count = self.count - 1
        return res

    def push(self, value):
        NewNode  = Node(value)
        NewNode.prev = self.stack
        self.stack = NewNode
        self.count = self.count + 1

    def peek(self):
        if self.size()== 0:
            return None # если стек пустой
        res  = self.stack.value
        return res

class Queue:
    def __init__(self):
        self.stackenqueue = Stack()
        self.stackdedequeue = Stack()

    def enqueue(self, item):
        self.stackenqueue.push(item)

    def dequeue(self):
        res = None
        if self.stackdedequeue.count>0:
            return self.stackdedequeue.pop()
        while self.stackenqueue.count >0:
            self.stackdedequeue.push(self.stackenqueue.pop())
        res =self.stackdedequeue.pop()
        return res # если очередь пустая

    def size(self):
        return self.stackenqueue.count + self.stackdedequeue.count


def goto(queue,n):
    for n in range(n):
        queue.enqueue(queue.dequeue())

