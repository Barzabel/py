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
        self.parenBranch = None  # True - право False - лево None - корень


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
                if res.Node.Parent == None:
                    res.parenBranch = None
                elif res.Node.Parent.LeftChild == res.Node:
                    res.parenBranch = False
                elif res.Node.Parent.RightChild == res.Node:
                    res.parenBranch = True
                return res

            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            elif Node.NodeKey > key:
                if Node.LeftChild is not None:

                    Node = Node.LeftChild
                else:
                    res.Node = Node
                    res.ToLeft = True
                    return res


            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            elif Node.NodeKey < key:

                if Node.RightChild is not None:

                    Node = Node.RightChild
                else:
                    res.Node = Node
                    res.ToLeft = False
                    return res
        return res

    def AddKeyValue(self, key, val):
        parent = self.FindNodeByKey(key)
        if parent.NodeHasKey == True and parent.Node is not None:
            return False
        elif parent.ToLeft == True and parent.Node is not None:

            NewNode = BSTNode(key, val, parent.Node)
            parent.Node.LeftChild = NewNode
        elif parent.ToLeft == False and parent.Node is not None:

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
        if parent.NodeHasKey == False:
            return False
        Node1 = parent.Node
        NodeParent = Node1.Parent
        Left = Node1.LeftChild

        # готовим новый узел
        if Node1.RightChild is not None:
            NewNode = self.__min(Node1.RightChild)
            if NewNode == Node1.RightChild:
                NewNode.LeftChild = Left
                if Left is not None:
                    Left.Parent = NewNode

            elif NewNode is not Node1.RightChild and NewNode.RightChild == None:
                NewNode.Parent.LeftChild = None
                NewNode.LeftChild = Left
                if Left is not None:
                    Left.Parent = NewNode


            elif NewNode is not Node1.RightChild and NewNode.RightChild is not None:
                NewNode.Parent.LeftChild = NewNode.RightChild
                NewNode.RightChild.Parent = NewNode.Parent
                NewNode.RightChild = None

                NewNode.RightChild = Node1.RightChild
                Node1.RightChild.parent = NewNode
                NewNode.LeftChild = Left
                if Left is not None:
                    Left.Parent = NewNode

            if parent.parenBranch == None:

                self.Root = NewNode
                NewNode.Parent = None
            elif parent.parenBranch == True:

                NodeParent.RightChild = NewNode
            elif parent.parenBranch == False:

                NodeParent.LeftChild = NewNode


        # ____________________________________________

        elif Node1.RightChild == None and Node1.LeftChild is not None:

            Left.Parent = Node1.Parent  #

            if parent.parenBranch == None:

                self.Root = Node1.LeftChild
                self.Root.Parent = None

            elif parent.parenBranch == True:

                NodeParent.RightChild = Node1.LeftChild
                Node1.LeftChild.Parent = NodeParent

            elif parent.parenBranch == False:

                NodeParent.LeftChild = Node1.LeftChild

                Node1.LeftChild.Parent = NodeParent


        # _________________________________________________________________

        elif Node1.RightChild == None and Node1.LeftChild == None:

            if parent.parenBranch == None:
                self.Root = None
            elif parent.parenBranch == True:
                NodeParent.RightChild = None
            elif parent.parenBranch == False:
                NodeParent.LeftChild = None

        return True

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

    def __count(self, Node):

        if Node.LeftChild is not None and Node.RightChild is not None:
            return 1 + self.__count(Node.LeftChild) + self.__count(Node.RightChild)
        elif Node.LeftChild == None and Node.RightChild is not None:
            return 1 + self.__count(Node.RightChild)
        elif Node.LeftChild is not None and Node.RightChild == None:
            return 1 + self.__count(Node.LeftChild)
        elif Node.LeftChild == None and Node.RightChild == None:  # Выход из рекурсии
            return 1

    def getList(self, Node):
        res = []
        if Node == None:
            return res

        if Node.RightChild is not None and Node.LeftChild is not None:
            res = self.getList(Node.RightChild) + [Node.NodeKey] + self.getList(Node.LeftChild)

        elif Node.RightChild is not None and Node.LeftChild == None:
            res = self.getList(Node.RightChild) + [Node.NodeKey]

        elif Node.RightChild == None and Node.LeftChild is not None:
            res = [Node.NodeKey] + self.getList(Node.LeftChild)

        elif Node.RightChild == None and Node.LeftChild == None:
            return [Node.NodeKey]

        return res