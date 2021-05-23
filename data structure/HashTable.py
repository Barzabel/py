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
        
        return index

    def find(self, value):
        start_hash_adress = self.hash_fun(value)

        for x in range(0, self.size, self.step):
            if self.slots[(start_hash_adress + x) % self.size] == value:
                return (start_hash_adress + x) % self.size
            elif self.slots[(start_hash_adress + x)%self.size] == None:
                return None
        return None




