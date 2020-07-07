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


    def gethead(self):
        return self.head.next

    def gettail(self):
        return self.tail.prev

    def add_in_tail(self, item):

        item.prev = self.tail.prev
        self.tail.prev.next = item
        self.tail.prev = item
        item.next = self.tail


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

                if all == False:
                    return

                node = node.next

            else:
                node = node.next

    def clean(self):
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):
        node = self.gethead()
        x = 0
        while node.dummy is not True:
            node = node.next
            x = x + 1
        return x

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

        else:
            if self.nodeinlist(afterNode)==False:
                return
            newNode.next = afterNode.next
            afterNode.next.prev = newNode
            newNode.prev = afterNode
            afterNode.next = newNode

    def add_in_head(self, newNode):
        newNode.next = self.head.next
        self.head.next.prev = newNode
        newNode.prev = self.head
        self.head.next = newNode




