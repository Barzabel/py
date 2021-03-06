




class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = []
        for x in range(size):
            self.vertex.append(Vertex(None))

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

    def WeakVertices(self):
        res = []
        for x in range(len(self.m_adjacency)):
            isWeak = True
            for y in [ v for v in range(len(self.m_adjacency[x])) if self.m_adjacency[x][v]==1]:
                for z in [ v for v in range(len(self.m_adjacency[x])) if self.m_adjacency[x][v]==1]:
                    if z != y and z!=x and y!=x and self.IsEdge(z,y) == True:
                        isWeak = False
            if isWeak == True:
                res.append(self.vertex[x])
        return res


