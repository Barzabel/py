class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        rez = []
        node = self.head
        while node is not None:
            if node.value == val:
                rez.append(node)
            node = node.next
        return rez

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val and node == self.head:
                if self.len() == 1:
                    self.clean()
                    return
                node.next.prev = None
                self.head = node.next

                if all == False:
                    return
                node = node.next

            elif node.value == val and node is not self.head and node is not self.tail:
                node.prev.next = node.next
                node.next.prev = node.prev

                if all == False:
                    return

                node = node.next

            elif node.value == val and node == self.tail:
                node.prev.next = None
                self.tail = node.prev

                if all == False:
                    return

                node = node.next

            else:
                node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        x = 0
        while node is not None:
            node = node.next
            x = x + 1
        return x

    def nodeinlist(self,node):
        iter1 = self.head
        while iter1 is not None:
            if iter1 == node:
                return True
            iter1 = iter1.next
        return False

    def insert(self, afterNode, newNode):

        if afterNode == None and self.len() == 0 :
            self.head = newNode
            newNode.prev = None
            newNode.next = None
            self.tail = newNode

        elif (afterNode == None and self.len() != 0)or(afterNode == self.tail):
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.tail.next = None

        else:
            if self.nodeinlist(afterNode)==False:
                return
            newNode.next = afterNode.next
            newNode.prev = afterNode
            afterNode.next = newNode


    def add_in_head(self, newNode):
        self.head.prev = newNode
        newNode.next = self.head
        newNode.prev = None
        self.head = newNode




