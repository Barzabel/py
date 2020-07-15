class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None
        self.dummy = False

class LinkedListPlus:
    def __init__(self):
        self.head = Node(None)
        self.head.dummy = True

        self.tail = Node(None)
        self.tail.dummy = True

        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0


    def gethead(self):
        return self.head.next

    def gettail(self):
        return self.tail.prev

    def add_in_tail(self, item):

        item.prev = self.tail.prev
        self.tail.prev.next = item
        self.tail.prev = item
        item.next = self.tail

        self.count = self.count + 1

    def pop_in_tail(self):
        if self.len()== 0:
            return None # если стек пустой
        res = self.gettail()
        res.prev.next = res.next
        res.next.prev = res.prev
        self.count = self.count - 1
        return res


    def add_in_head(self, newNode):
        newNode.next = self.head.next
        self.head.next.prev = newNode
        newNode.prev = self.head
        self.head.next = newNode

        self.count = self.count + 1

    def pop_in_head(self):

        if self.len()== 0:
            return None # если стек пустой
        res = self.gethead()
        res.prev.next = res.next
        res.next.prev = res.prev
        self.count = self.count - 1
        return res


    def find(self, val):

        node = self.gethead()
        while node.dummy is not True:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):

        rez = []
        node = self.gethead()
        while node.dummy is not True:
            if node.value == val:
                rez.append(node)
            node = node.next
        return rez

    def delete(self, val, all=False):

        node = self.gethead()
        while node.dummy is not True:

            if node.value == val :
                node.prev.next = node.next
                node.next.prev = node.prev
                self.count = self.count - 1
                if all == False:
                    return

                node = node.next

            else:
                node = node.next

    def clean(self):
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def len(self):

        return self.count

    def nodeinlist(self,node):
        iter1 = self.gethead()
        while iter1.dummy is not True:
            if iter1 == node:
                return True
            iter1 = iter1.next
        return False

    def insert(self, afterNode, newNode):

        if afterNode == None:

            self.tail.prev.next = newNode
            newNode.prev = self.tail.prev
            newNode.next = self.tail
            self.tail.prev = newNode

            self.count = self.count + 1

        else:
            if self.nodeinlist(afterNode)==False:
                return
            newNode.next = afterNode.next
            afterNode.next.prev = newNode
            newNode.prev = afterNode
            afterNode.next = newNode

            self.count = self.count + 1






class Deque:
    def __init__(self):
        self.list1 = LinkedListPlus()

    def addFront(self, item):
        NewNode = Node(item)
        self.list1.add_in_head(NewNode)



    def addTail(self, item):
        NewNode = Node(item)
        self.list1.add_in_tail(NewNode)

    def removeFront(self):
        if self.list1.len()== 0:
            return None
        return self.list1.pop_in_head().value

    def removeTail(self):
        if self.list1.len()== 0:
            return None
        return self.list1.pop_in_tail().value

    def size(self):
        return self.list1.len()




def ispalindrom(val):
    a = Deque()
    for x in val:
        a.addTail(x)
    while a.size()>1:
        tail = a.removeTail()
        head = a.removeFront()
        if (tail != head):
            return False
    return True

