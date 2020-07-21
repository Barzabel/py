class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):

        res = BSTFind()
        Node = self.Root
        while Node is not None:
            if Node.NodeKey == key:
                res.Node = Node
                res.NodeHasKey = True
                return res

        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            elif Node.NodeKey > key:
                if Node.LeftChild is not None:
                    Node = Node.LeftChild
                else:
                    res.Node = Node
                    return res


        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            elif Node.NodeKey < key:
                if Node.RightChild is not None:
                    Node = Node.RightChild
                else:
                    res.Node = Node
                    res.ToLeft = True
                    return res
        return res




    def AddKeyValue(self, key, val):
        parent = self.FindNodeByKey(key)
        if parent.NodeHasKey == True and parent.Node is not None:
            return False
        elif parent.ToLeft and parent.Node is not None:
            NewNode = BSTNode(key, val, parent.Node)
            parent.Node.LeftChild = NewNode
        elif parent.ToLeft==False and parent.Node is not None:
            NewNode = BSTNode(key, val, parent.Node)
            parent.Node.RightChild = NewNode
        elif parent.Node == None:
            NewNode = BSTNode(key, val, None)
            self.Root = NewNode

    def FinMinMax(self, FromNode, FindMax):
        if FindMax:
            return self.__max(FromNode)
        else:
            return self.__min(FromNode)

    def DeleteNodeByKey(self, key):
        parent = self.FindNodeByKey(key)
        if parent.NodeHasKey == True and parent.Node is not None:
            return False
        return False  # если узел не найден

    def Count(self):
        if self.Root == None:
            return 0  # количество узлов в дереве
        else:
            return self.__count(self.Root)


    def __max(self, Node):
        Node1 = Node
        while Node1.RightChild is not None:
            Node1 = Node1.RightChild

        return Node1

    def __min(self, Node):
        Node1 = Node
        while Node1.LeftChild is not None:
            Node1 = Node1.LeftChild
        return Node1

    def __count(self,Node):

        if Node.LeftChild is not None and Node.RightChild is not None:
            return 1 + self.__count(Node.LeftChild) + self.__count(Node.RightChild)
        elif Node.LeftChild == None and Node.RightChild is not None:
            return 1 + self.__count(Node.RightChild)
        elif Node.LeftChild is not None and Node.RightChild == None:
            return 1 + self.__count(Node.LeftChild)
        elif Node.LeftChild == None and Node.RightChild == None: #Выход из рекурсии
            return 1