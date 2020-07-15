import unittest

class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        a = str(value)
        res = 0
        for x in range(len(a)):
            res = (res//5+ord(a[x]))*13 + 7
        return res % self.size

    def seek_slot(self, value):
        hash1 = self.hash_fun(value)
        index = None

        for x in range(0,self.size,self.step):
            if self.slots[(hash1+x)%self.size] == None:
                index = (hash1+x)%self.size
                break
        return index

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value


    def find(self, value):
        hash1 = self.hash_fun(value)

        for x in range(0,self.size,self.step):
            if self.slots[(hash1+x)%self.size] == value:
                return (hash1+x)%self.size
            elif self.slots[(hash1+x)%self.size] == None:
                return None
        return None





class TesHashTable(unittest.TestCase):

    def setUp(self):
        self.HashTable1 = HashTable(10, 1)
        self.HashTable2 = HashTable(100, 4)
        self.HashTable3 = HashTable(1000, 7)

    def test_hash_fun(self):
        self.assertEqual(self.HashTable1.seek_slot(1), self.HashTable1.hash_fun(1))
        self.assertEqual(self.HashTable2.seek_slot(1), self.HashTable2.hash_fun(1))
        self.assertEqual(self.HashTable3.seek_slot(1), self.HashTable3.hash_fun(1))



    def test_seek_slot(self):
        self.HashTable1.put(1)
        self.HashTable2.put(1)
        self.HashTable3.put(1)

        self.assertTrue(self.HashTable1.find(1) is not None)
        self.assertTrue(self.HashTable2.find(1) is not None)
        self.assertTrue(self.HashTable3.find(1) is not None)

        self.assertFalse(self.HashTable1.seek_slot(1) == self.HashTable1.hash_fun(1))
        self.assertFalse(self.HashTable2.seek_slot(1) == self.HashTable2.hash_fun(1))
        self.assertFalse(self.HashTable3.seek_slot(1) == self.HashTable3.hash_fun(1))

        for x in range(10):
            self.HashTable1.put(1)
            self.HashTable2.put(1)
            self.HashTable3.put(1)

        self.assertTrue(self.HashTable1.seek_slot(1) == None)
        self.assertTrue(self.HashTable2.seek_slot(1) is not None)
        self.assertTrue(self.HashTable3.seek_slot(1) is not None)

        for x in range(100):
            self.HashTable1.put(1)
            self.HashTable2.put(1)
            self.HashTable3.put(1)

        self.assertTrue(self.HashTable1.seek_slot(1) == None)
        self.assertTrue(self.HashTable2.seek_slot(1) == None)
        self.assertTrue(self.HashTable3.seek_slot(1) is not None)

        for x in range(1000):
            self.HashTable1.put(1)
            self.HashTable2.put(1)
            self.HashTable3.put(1)

        self.assertTrue(self.HashTable1.seek_slot(1) == None)
        self.assertTrue(self.HashTable2.seek_slot(1) == None)
        self.assertTrue(self.HashTable3.seek_slot(1) == None)


    def test_find(self):
        self.HashTable1.put(1)
        self.HashTable2.put(1)
        self.HashTable3.put(1)

        self.assertTrue(self.HashTable1.find(1) is not None)
        self.assertTrue(self.HashTable2.find(1) is not None)
        self.assertTrue(self.HashTable3.find(1) is not None)

        self.HashTable1.slots[self.HashTable1.find(1)] = None
        self.HashTable2.slots[self.HashTable2.find(1)] = None
        self.HashTable3.slots[self.HashTable3.find(1)] = None

        self.assertTrue(self.HashTable1.find(1) == None)
        self.assertTrue(self.HashTable2.find(1) == None)
        self.assertTrue(self.HashTable3.find(1) == None)

    def test_put(self):

        self.assertEqual(self.HashTable1.seek_slot(1), self.HashTable1.hash_fun(1))
        self.assertEqual(self.HashTable2.seek_slot(1), self.HashTable2.hash_fun(1))
        self.assertEqual(self.HashTable3.seek_slot(1), self.HashTable3.hash_fun(1))
        
        self.HashTable1.put(1)
        self.HashTable2.put(1)
        self.HashTable3.put(1)

        self.assertTrue(self.HashTable1.find(1) is not None)
        self.assertTrue(self.HashTable2.find(1) is not None)
        self.assertTrue(self.HashTable3.find(1) is not None)

        self.assertFalse(self.HashTable1.seek_slot(1) == self.HashTable1.hash_fun(1))
        self.assertFalse(self.HashTable2.seek_slot(1) == self.HashTable2.hash_fun(1))
        self.assertFalse(self.HashTable3.seek_slot(1) == self.HashTable3.hash_fun(1))



if __name__ == "__main__":
  unittest.main()