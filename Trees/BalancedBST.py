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


           # сбалансировано ли дерево с корнем root_node




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

