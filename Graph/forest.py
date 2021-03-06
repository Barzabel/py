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
        grafs = []

        arr = self.GetAllNodes()
        graf = self.__getgrafchid(self.Root)
        y = 0
        sumusel = [x for x in range(1,len(arr),2)]

        sumR = 1




        while sumR <len(arr):
            indexus = len(graf.m_adjacency) - 1
            parent = None
            for x in range(len(graf.m_adjacency) - 1, -1, -1):
                for c in range(indexus):
                    if graf.m_adjacency[x][c] == 1:
                        parent = c

                if  sum(graf.m_adjacency[x][:indexus]) ==1 and len(graf.m_adjacency[x][:indexus])%2==0 and sum(graf.m_adjacency[x][indexus:]) %2 ==1:

                    graf.RemoveEdge(x, parent)
                    res.append(arr[parent])
                    res.append(arr[x])
                    sumR = 1

                    break
                indexus = indexus-1




            sumR = sumR +2


        return res

    def __getgrafchid(self, node):
        arr = self.__GetAllNodes(node)

        g = SimpleGraph(self.__recount(node))
        for x in range(self.__recount(node)):
            g.AddVertex(x)
        for x in range(self.__recount(node)):
            for c in arr[x].Children:
                g.AddEdge(x, arr.index(c))

        return g
