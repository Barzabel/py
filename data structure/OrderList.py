

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascendin = asc
        self.count = 0



    def compare(self, v1, v2):
        if (v1 < v2):
            return -1
        elif (v1 > v2):
            return 1
        else:
            return  0




    def add(self, value):
        NewNode = Node(value)
        if self.head is None:
            self.head = NewNode
            self.tail = NewNode
            self.count = self.count + 1
            return
        Node1 = self.tail



        while Node1 is not None:
            if self.__ascendin:
                if self.compare(NewNode.value,Node1.value)>0 :
                    self.__insert(Node1,NewNode)
                    self.count = self.count + 1
                    return
            else:
                if self.compare(Node1.value,NewNode.value)>0 :
                    self.__insert(Node1,NewNode)
                    self.count = self.count + 1
                    return
            Node1 = Node1.prev


        self.add_in_head(NewNode)



    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            newNode.prev = None
            newNode.next = None
            self.count = self.count + 1
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            self.count = self.count + 1


    def __insert(self, afterNode, newNode):



        if afterNode == self.tail:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.tail.next = None

        else:

            newNode.next = afterNode.next
            afterNode.next.prev = newNode
            newNode.prev = afterNode
            afterNode.next = newNode


    def find(self, val):
        node1 = self.head
        while node1 is not None:
            if node1.value == val:
                return node1
            if node1.value > val and self.__ascendin:
                return None
            if node1.value < val and self.__ascendin != True:
                return None
            node1 = node1.next

        return None

    def delete(self, val):
        node = self.head
        while node is not None:
            if node.value == val and node == self.head:
                if self.len() == 1:
                    self.clean(self.__ascendin)
                    return
                node.next.prev = None
                self.head = node.next
                self.count = self.count - 1

                return
                node = node.next

            elif node.value == val and node is not self.head and node is not self.tail:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.count = self.count - 1
                return
                node = node.next

            elif node.value == val and node == self.tail:
                node.prev.next = None
                self.tail = node.prev
                self.count = self.count - 1
                return
                node = node.next

            else:
                node = node.next

    def clean(self, asc):
        self.__ascendin = asc
        self.count = 0
        self.head = None
        self.tail = None

    def len(self):
        res = self.count
        return res

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, V1, V2):
        v1 = V1.strip()
        v2 = V2.strip()
        if (v1 < v2):
            return -1
        elif (v1 > v2):
            return 1
        else:
            return  0























