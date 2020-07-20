
import numpy


class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def __Hash(self,value):
        a = str(value)
        res = 0
        for x in range(len(a)):
            res = (res // 5 + ord(a[x])) * 13 + 7
        return res % self.size

    def hash_fun(self, key):
         res =  self.__Hash(key)
         index = None
         for x in range(0, self.size, 1):
             if self.slots[(res + x) % self.size] == None or self.slots[(res + x) % self.size] == key:
                 index = (res + x) % self.size
                 break
         return index

    def is_key(self, key):
        hash1 = self.__Hash(key)

        for x in range(0, self.size, 1):
            if self.slots[(hash1 + x) % self.size] == key:
                return True
        return False

    def get(self, key):
        hash1 = self.__Hash(key)
        for x in range(0, self.size, 1):
            if self.slots[(hash1 + x) % self.size] == key:
                self.hits[(hash1 + x) % self.size] = self.hits[(hash1 + x) % self.size] + 1
                return self.values[(hash1 + x) % self.size]

        return None

    def put(self, key, value):

        index = self.hash_fun(key)

        if index == None:
            index = numpy.argmin(self.hits)
            self.hits[index] = 0

        self.slots[index] = key
        self.values[index] = value




