class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи


    def MakeHeap(self, a, depth):
        self.depth =  depth
        i = 2**(depth+1)-1

        self.HeapArray = [None]*i

        for x in a:
            self.Add(x)




        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        pass

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        pos = self.getfordel()
        if pos == -1:
            return -1  # если куча пуста
        res = self.HeapArray[0]
        self.HeapArray[0]=self.HeapArray[pos]
        self.HeapArray[pos] = None
        index = 0
        child1 = 1
        child2 = 2
        newindex = None
        while True:
            if self.HeapArray[child1]==None and self.HeapArray[child2] == None:
                break
            elif self.HeapArray[child1]==None and self.HeapArray[index]>self.HeapArray[child2]:
                break
            elif self.HeapArray[child2]==None and self.HeapArray[index]>self.HeapArray[child1]:
                break
            elif (index==pos) or (self.HeapArray[index]>self.HeapArray[child1]and self.HeapArray[index]>self.HeapArray[child2]):
                break
            else:
                if self.HeapArray[child1]>self.HeapArray[child2]:
                    newindex = child1
                else:
                    newindex = child2
                b = self.HeapArray[index]
                self.HeapArray[index] = self.HeapArray[newindex]
                self.HeapArray[newindex] = b
                index = newindex
                child1 = index*2 + 1
                child2 = index*2 + 2
        return res




    def Add(self, key):
        pos = self.getpos()
        if pos == -1:#!!!!!!!!!!!!!!!!!
            return False # если куча вся заполнена
        self.HeapArray[pos]=key
        if pos % 2 == 0:
            parent = (pos - 2) // 2
        else:
            parent = (pos - 1) // 2
        index = pos

        while True:
            if (index==0) or (self.HeapArray[index]<=self.HeapArray[parent]):
                break
            else:
                b = self.HeapArray[index]
                self.HeapArray[index] = self.HeapArray[parent]
                self.HeapArray[parent] = b
            index = parent
            if parent%2 == 0:
                parent  = (parent-2) // 2
            else:
                parent = (parent-1) // 2
        return True
    def getpos(self):
        i = 0
        while i < len(self.HeapArray):
            if self.HeapArray[i] == None:
                return i
            else:
                i= i +1
        return -1

    def getfordel(self):
        i = len(self.HeapArray)-1
        while i >=0:
            if self.HeapArray[i] is not None:
                return i
            else:
                i= i -1
        return -1



