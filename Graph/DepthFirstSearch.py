
class Node:
    def __init__(self,val):
        self.value = val
        self.prev = None


class Stack:
    def __init__(self):
        self.stack = None
        self.count = 0

    def size(self):
        return self.count

    def pop(self):
        if self.size()== 0:
            return None # если стек пустой
        res  = self.stack.value
        self.stack = self.stack.prev
        self.count = self.count - 1
        return res


    def push(self, value):
        NewNode  = Node(value)
        NewNode.prev = self.stack
        self.stack = NewNode
        self.count = self.count + 1

    def peek(self):
        if self.size()== 0:
            return None # если стек пустой
        res  = self.stack.value
        return res




class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


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




    def __StackDepthFirstSearch(self, VFrom, VTo):

        for x in self.vertex:
            x.Hit = False

        res = Stack()

        self.vertex[VFrom].Hit = True

        res.push(VFrom)
        v = VFrom

        while True:
            fershin = [ x for x in range(len(self.m_adjacency[v])) if self.m_adjacency[v][x]==1 and self.vertex[x].Hit == False]
            for x in fershin:
                if x==VTo:
                    res.push(x)

                    return res

                elif self.vertex[x].Hit == False:
                    res.push(x)
                    self.vertex[x].Hit = True
                    v = x
                    break

            if len(fershin)==0:

                v = res.pop()
                if v == None:

                    return res



        return res


    def DepthFirstSearch(self, VFrom, VTo):
        res = []
        steck = self.__StackDepthFirstSearch( VFrom, VTo)
        while steck.peek() is not None:

            res.append(steck.pop())
        res.reverse()
        return res
# узлы задаются позициями в списке vertex
# возвращается список узлов -- путь из VFrom в VTo
# или [] если пути нету


# узлы задаются позициями в списке vertex
# возвращается список узлов -- путь из VFrom в VTo
# или [] если пути нету




