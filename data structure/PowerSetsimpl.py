class PowerSet:

    def __init__(self):
        self.slots = []


    def size(self):
        return len(self.slots)
        # количество элементов в множестве

    def put(self, value):
        if(value in self.slots):
            return
        self.slots.append(value)
        # всегда срабатывает

    def get(self, value):
        if(value in self.slots):
            return True
        return False

    def remove(self, value):
        if (value in self.slots):
            self.slots.remove(value)
            return True
        return False

    def intersection(self, set2):
        res = PowerSet()
        values2 = [x for x in set2.slots if x is not None]
        values1 = [x for x in self.slots if x is not None and x in  values2]
        for x in values1:
            res.put(x)
        # пересечение текущего множества и set2
        return res

    def union(self, set2):
        res = PowerSet()
        values1 = [x for x in self.slots if x is not None]
        values2 = [x for x in set2.slots if x is not None and x not in values1]

        for x in values1:
            res.put(x)
        for x in values2:
            res.put(x)
        return res

    def difference(self, set2):

        res = PowerSet()
        values1 = [x for x in self.slots ]
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
