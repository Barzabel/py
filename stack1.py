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




