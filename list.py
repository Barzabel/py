class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

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
        node1 = Node(1)
        node1.next = self.head
        node2 = self.head

        while node2 is not None:
            if node2.value == val and node2 == self.head:
                if self.head.next == None:
                    self.tail = self.head
                self.head = self.head.next
                node1 = Node(None)
                node1.next = self.head
                node2 = self.head

                continue

            if node2.value == val and node2.next is not None:
                node1.next = node2.next
                node2 = node2.next

                continue

            if node2.value == val and node2 == self.tail:
                node1.next = None
                self.tail == node1

            node1 = node2
            node2 = node2.next

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

    def insert(self, afterNode, newNode):
        newNode.next = afterNode.next
        afterNode.next = newNode





