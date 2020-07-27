class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a):
        a.sort()
        self.Root = BSTNode(a[len(a)//2],None)
        self.Root.Level = 1


        self.__addleft(self.Root,a[:len(a)//2])
        self.__addright(self.Root, a[len(a) // 2+1:])



    # создаём дерево с нуля из неотсортированного массива a
    # ...
    def __addleft(self,parent,a):
        if len(a)== 0:
            return
        Node = BSTNode(a[len(a)//2],parent)
        Node.Level = parent.Level+1
        parent.LeftChild = Node
        if len(a) == 1:
            return
        self.__addleft(Node, a[:len(a) // 2])
        self.__addright(Node, a[len(a) // 2+1:])

    def __addright(self, parent, a):

        if len(a) == 0:
            return


        Node = BSTNode(a[len(a) // 2], parent)
        Node.Level = parent.Level + 1
        parent.RightChild = Node
        if len(a) == 1:
            return
        self.__addleft(Node, a[:len(a) // 2])
        self.__addright(Node, a[len(a) // 2+1:])

    def IsBalanced(self, root_node):
        if self.__IsBalanced1(root_node):
            pass
        else:
            return False
        res = True
        if root_node.RightChild is not None and root_node.LeftChild is not None:
            if root_node.RightChild.NodeKey >= root_node.NodeKey  and root_node.LeftChild.NodeKey < root_node.NodeKey:
                res = res * self.IsBalanced(root_node.RightChild) * self.IsBalanced(root_node.LeftChild)
            else:
                return False
        elif root_node.RightChild == None and root_node.LeftChild is not None:
            if root_node.LeftChild.NodeKey < root_node.NodeKey:
                res = res * self.IsBalanced(root_node.LeftChild)
            else:
                return False
        elif root_node.RightChild is not None and root_node.LeftChild == None:
            if root_node.RightChild.NodeKey >= root_node.NodeKey:
                res = res * self.IsBalanced(root_node.RightChild)
            else:
                return False
        elif root_node.RightChild == None and root_node.LeftChild == None:
            return True
        return res

    def __IsBalanced1(self,node):
        left = self.__maxLright(node)
        right = self.__maxLleft(node)
        if  ((left-right)>1)and((right-left)>1):
            return False
        else:
            return True

    def __maxLright(self, Node):
        Node1 = Node
        while Node1.RightChild is not None:
            Node1 = Node1.RightChild

        return Node1.Level

    def __maxLleft(self, Node):
        Node1 = Node
        while Node1.LeftChild is not None:
            Node1 = Node1.LeftChild
        return Node1.Level

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


