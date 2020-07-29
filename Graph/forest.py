class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [Vertex(None)] * size

    def AddVertex(self, v):


        if v < self.max_vertex and self.vertex[v].Value == None:
            self.vertex[v].Value = v
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex


        # здесь и далее, параметры v -- индекс вершины

    # в списке  vertex
    def RemoveVertex(self, v):
        # ваш код удаления вершины со всеми её рёбрами
        if self.vertex[v].Value  == None:
            return
        for x in self.vertex:
            if x.Value is not None:
                self.RemoveEdge(v,self.vertex.index(x))
        self.vertex[v].Value= None



    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        if self.vertex[v1].Value is not None and self.vertex[v1].Value is not None:
            if self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1:
                return True
        return False

    def AddEdge(self, v1, v2):
        if self.vertex[v1].Value is not None and self.vertex[v1].Value is not None:
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1
        # добавление ребра между вершинами v1 и v2


    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        if self.vertex[v1].Value is not None and self.vertex[v1].Value is not None:
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0



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

        return self.__FindNodesByValue(self.Root, val)

    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode.Parent is not None:
            OriginalNode.Parent.Children.remove(OriginalNode)

        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent = NewParent

    def Count(self):
        res = self.__recount(self.Root)

        return res

    def LeafCount(self):
        res = self.__reLeafCount(self.Root)
        return res

    def __recount(self, NodeTre):
        res = 0
        if len(NodeTre.Children) == 0:
            return 1
        else:
            res = res + 1
            for x in NodeTre.Children:
                res = res + self.__recount(x)
        return res

    def __reLeafCount(self, NodeTre):
        res = 0
        if len(NodeTre.Children) == 0:
            return 1
        else:
            for x in NodeTre.Children:
                res = res + self.__reLeafCount(x)
        return res

    def __FindNodesByValue(self, Node, val):
        res = []
        if Node.NodeValue == val:
            res.append(Node)
        if len(Node.Children) > 0:
            for x in Node.Children:
                for y in self.__FindNodesByValue(x, val):
                    res.append(y)
        return res

    def __GetAllNodes(self, Node):
        res = []

        res.append(Node)
        if len(Node.Children) > 0:
            for x in Node.Children:
                for y in self.__GetAllNodes(x):
                    res.append(y)
        return res




    def EvenTrees(self):
        res = []
        g = SimpleGraph(self.Count())
        nods = self.GetAllNodes()
        for x in range(self.Count()):
            g.AddVertex(x)
        for x in range(self.Count()):
            for c in nods[x].Children:
                g.AddEdge(x, nods.index(c))

        iter = True
        linesum = 2
        linesum2 = 2
        while linesum<len(nods):
            for x in range(len(g.m_adjacency)):
                if sum(g.m_adjacency[x]) == linesum :
                    while linesum2 < len(nods):
                        for y in range(len(g.m_adjacency[x])):
                            
                            if g.m_adjacency[x][y] == 1 and sum([c[y] for c in g.m_adjacency]) == linesum2:
                                res.append(nods[x])
                                res.append(nods[y])
                                g.RemoveEdge(x, y)
                                linesum2 = 2
                                linesum = 2
                                break
                        linesum2 = linesum2+2
            linesum = linesum +2

        return res













