import unittest

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


class TesPowerSet(unittest.TestCase):

    def setUp(self):
        self.PowerSet = PowerSet()
        self.PowerSet1 = PowerSet()
        self.PowerSet2 = PowerSet()

    def test_put(self):

        self.assertTrue(self.PowerSet.size() ==0)
        for x in range(90000):
            self.PowerSet.put(1)
        self.assertTrue(self.PowerSet.size() == 1)
        self.assertTrue(self.PowerSet.get(1) == True)
        for x in range(100):
            self.PowerSet.put(x)
        for x in range(100):
            self.PowerSet.put(x)
        self.assertTrue(self.PowerSet.size() == 100)
        for x in range(100):
            self.assertTrue(self.PowerSet.get(x) == True)

        self.assertEqual(1,1 )
        self.assertFalse(False)

    def test_remove(self):
        for x in range(100):
            self.PowerSet.put(x)
        for x in range(100):
            self.PowerSet.remove(x)

    def test_intersection1(self):
        for x in range(100):
            self.PowerSet1.put(x)
        for x in range(100):
            self.PowerSet2.put(x)
        self.PowerSet = self.PowerSet1.intersection(self.PowerSet2)
        for x in range(100):
            self.assertTrue(self.PowerSet.get(x) == True)
        self.assertTrue(self.PowerSet.size() == 100)

    def test_intersection2(self):

        for x in range(100):
            self.PowerSet1.put(x)
        for x in range(100,200,1):
            self.PowerSet2.put(x)
        self.PowerSet = self.PowerSet1.intersection(self.PowerSet2)

        for x in range(100):
            self.assertTrue(self.PowerSet.get(x) == False)
        self.assertTrue(self.PowerSet.size() == 0)

    def test_union1(self):
        for x in range(100):
            self.PowerSet1.put(x)
        for x in range(100):
            self.PowerSet2.put(x)
        self.PowerSet = self.PowerSet1.union(self.PowerSet2)

        for x in range(100):
            self.assertTrue(self.PowerSet.get(x) == True)
        self.assertTrue(self.PowerSet.size() == 100)
        self.assertTrue(self.PowerSet.get(101) == False)

    def test_union2(self):
        for x in range(100):
            self.PowerSet1.put(x)
        for x in range(100,200,1):
            self.PowerSet2.put(x)
        self.PowerSet = self.PowerSet1.union(self.PowerSet2)

        for x in range(200):
            self.assertTrue(self.PowerSet.get(x) == True)
        self.assertTrue(self.PowerSet.size() == 200)

    def test_difference1(self):
        for x in range(100):
            self.PowerSet1.put(x)
        for x in range(100):
            self.PowerSet2.put(x)
        self.PowerSet = self.PowerSet1.difference(self.PowerSet2)

        for x in range(100):
            self.assertTrue(self.PowerSet.get(x) == False)
        self.assertTrue(self.PowerSet.size() == 0)

    def test_difference2(self):
        for x in range(100):
            self.PowerSet1.put(x)
        for x in range(100,200,1):
            self.PowerSet2.put(x)
        self.PowerSet = self.PowerSet1.difference(self.PowerSet2)

        for x in range(100):
            self.assertTrue(self.PowerSet.get(x) == True)
        self.assertTrue(self.PowerSet.size() == 100)
        for x in range(100,200,1):
            self.assertTrue(self.PowerSet.get(x) == False)







unittest.main()
