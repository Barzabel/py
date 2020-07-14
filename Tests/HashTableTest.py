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



def testput():
    size = 10
    step  = 1
    hastable = HashTable(size,step )

    if hastable.hash_fun(1) != hastable.seek_slot(1):
        return False

    hastable.put(1)

    if hastable.hash_fun(1) == hastable.seek_slot(1):
        return False

    if hastable.hash_fun(1) != hastable.find(1):
        return False

    for x in range(size+1):
        hastable.put(1)

    if hastable.seek_slot(1) != None:
        return False


    return True



print(testput())