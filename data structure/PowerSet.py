"""
реализовано "множество" на основе ранее написанного класса HashTable.



"""


class HashTable:
    def __init__(self, sz, stp):
        self.size1 = sz
        self.step = stp
        self.slots = [None] * self.size1

    def hash_fun(self, value):
        a = str(value)
        res = 0
        for x in range(len(a)):
            res = (res//5+ord(a[x]))*13 + 7
        return res % self.size1

    def seek_slot(self, value):
        hash1 = self.hash_fun(value)
        index = None

        for x in range(0,self.size1,self.step):
            if self.slots[(hash1+x)%self.size1] == None:
                index = (hash1+x)%self.size1
                break
        return index

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value


    def find(self, value):
        hash1 = self.hash_fun(value)

        for x in range(0,self.size1,self.step):
            if self.slots[(hash1+x)%self.size1] == value:
                return (hash1+x)%self.size1
            elif self.slots[(hash1+x)%self.size1] == None:
                return None
        return None







class PowerSet(HashTable):

    def __init__(self):
        self.__sz = 50
        self.__stp = 3
        super().__init__( self.__sz, self.__stp)
        self.count = 0

    def size(self):

        return self.count
        

    def put(self, value):

        if self.get(value):
            return

        if self.seek_slot(value)==None:

            values =  [ x for x in  self.slots if x is not None]
            self.__sz = int(self.__sz * 1.33)
            super().__init__(self.__sz, self.__stp)
            for x in values:
                super(PowerSet, self).put(x)
            super(PowerSet, self).put(value)
            self.count = self.count + 1
        else:
            super(PowerSet, self).put(value)
            self.count = self.count + 1


    def getslots(self):
        return [ x for x in  self.slots if x is not None]

    def get(self, value):
        if self.find(value) is not None:
            return True
        return False

    def remove(self, value):
        if self.get(value) == False:
            return False
        else:
            values = [x for x in self.slots if x is not None and x != value]
            super().__init__(self.__sz, self.__stp)
            for x in values:
                super(PowerSet, self).put(x)
            self.count = self.count - 1
            return True
        # возвращает True если value удалено
        # иначе False


    def intersection(self, set2):
        res = PowerSet()
        values1 = [x for x in self.slots if x is not None and x in set2.slots]
        values2 = [x for x in set2.slots if x is not None and x in self.slots]

        for x in values1:
            res.put(x)
        for x in values2:
            res.put(x)



        return res
        # пересечение текущего множества и set2


    def union(self, set2):
        res = PowerSet()
        values1 = [x for x in self.slots if x is not None ]
        values2 = [x for x in set2.slots if x is not None and x not in values1 ]

        for x in values1:
            res.put(x)
        for x in values2:
            res.put(x)


        # объединение текущего множества и set2

        return res

    def difference(self, set2):

        res = PowerSet()
        values1 = [x for x in self.slots if x is not None]
        values2 = [x for x in values1 if x not in set2.slots]


        for x in values2:
            res.put(x)



        return res
        # разница текущего множества и set2


    def issubset(self, set2):
        for x in set2.slots:

            if x not in self.slots:
                return False
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        return True


