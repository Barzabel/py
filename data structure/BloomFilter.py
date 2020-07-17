
from bitarray import bitarray


class BloomFilter:

    def __init__(self, f_len):

        self.filter_len = f_len
        self.bit_array = bitarray()
        self.bit_array.extend([0 for x in range(self.filter_len)])
        self.m = f_len//2
        # создаём битовый массив длиной f_len ...


    def hash1(self, str1):
        str1 = str(str1)
        res = bitarray()
        res.extend([0 for x in range(self.filter_len)])
        hash = 0
        for c in str1:
            hash = (((hash + 7)//2) * (ord(c)//3)) % self.filter_len

        res[hash%self.m] = 1
        return res


    def hash2(self, str1):

        str1 = str(str1)
        res = bitarray()
        res.extend([0 for x in range(self.filter_len)])
        hash = 0
        for c in str1:
            hash = ((hash+1) * ord(c)) % self.filter_len


        if self.filter_len%2==1:
            res[hash % (self.m+1) + self.m] = 1
        else:
            res[hash%self.m + self.m] = 1

        return res

    def add(self, str1):

        self.bit_array = self.bit_array | (self.hash2(str1) | self.hash1(str1))

    def is_value(self, str1):
        if (self.bit_array == (self.bit_array|(self.hash2(str1) | self.hash1(str1)))  ):
            return True
        else:
            return False
    def print(self):
        print(self.bit_array)




