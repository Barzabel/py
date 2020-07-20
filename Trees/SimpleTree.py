class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):


        self.Root = root;  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        parent = NodeToDelete.Parent
        for x in NodeToDelete.Children:
            x.Parent = parent
            parent.Children.append(x)
        parent.Children.remove(NodeToDelete)

    def GetAllNodes(self):
        # ваш код выдачи всех узлов дерева в определённом порядке
        return self.__GetAllNodes(self.Root)

    def FindNodesByValue(self, val):

        return self.__FindNodesByValue(self.Root,val)

    def MoveNode(self, OriginalNode, NewParent):
        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent = NewParent


    def Count(self):
        res = self.__recount(self.Root)


        return res

    def LeafCount(self):
        res = self.__reLeafCount(self.Root)
        return res

    def __recount(self,NodeTre):
        res = 0
        if len(NodeTre.Children) == 0:
            return 1
        else:
            res = res +1
            for x in NodeTre.Children:

                res = res + self.__recount(x)
        return res

    def __reLeafCount(self,NodeTre):
        res = 0
        if len(NodeTre.Children) == 0:
            return 1
        else:
            for x in NodeTre.Children:

                res = res + self.__reLeafCount(x)
        return res

    def __FindNodesByValue(self,Node,val):
        res = []
        if Node.NodeValue == val:
            res.append(Node)
        if len(Node.Children)>0:
            for x in Node.Children:
                for y in self.__FindNodesByValue(x,val):
                    res.append(y)
        return res

    def __GetAllNodes(self,Node):
        res = []

        res.append(Node)
        if len(Node.Children)>0:
            for x in Node.Children:
                for y in self.__GetAllNodes(x):
                    res.append(y)
        return res












