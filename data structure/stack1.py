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


def postpr(st):
    res = None
    ar = st.split(" ")
    ar = [x for x in ar if x != '']
    stack1 = Stack()
    stack2 = Stack()

    for x in ar:
        stack2.push(x)

    while stack2.count > 0:
        stack1.push(stack2.pop())

    while stack1.count > 0:
        if stack1.peek() != "*" and stack1.peek() != "+" and stack1.peek() != "/" and stack1.peek() != "-" and stack1.peek() != "=":
            stack2.push(stack1.pop())


        else:
            if stack1.peek() == "*":
                stack2.push(float(stack2.pop()) * float(stack2.pop()))

                stack1.pop()
            elif stack1.peek() == "+":
                stack2.push(float(stack2.pop()) + float(stack2.pop()))
                stack1.pop()
            elif stack1.peek() == "-":
                a = stack2.pop()
                stack2.push(float(stack2.pop()) - float(a))
                stack1.pop()
            elif stack1.peek() == "/":
                a = stack2.pop()
                stack2.push(float(stack2.pop()) / float(a))
                stack1.pop()
            elif stack1.peek() == "=":
                res = stack2.peek()
                stack1.pop()
    res = stack2.peek()
    return res


print(postpr("8 2 + 10 + 12 * 44 - ="))


