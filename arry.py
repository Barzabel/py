import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)

        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity


    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):

        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        if self.count == self.capacity:
            self.resize(2*self.capacity)
        new_array = self.make_array(self.capacity)

        for x in range(i):
            new_array[x] = self.array[x]

        new_array[i] = itm


        for x in range(i,self.count):
            new_array[x+1] = self.array[x]

        self.array = new_array

        self.count = self.count + 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        
        if (self.count - 1) == int(self.capacity/2) and self.capacity > 16 :

            if int(self.capacity/1.5) < 16:
                self.resize(16)
            else:
                self.resize(int(self.capacity/1.5))
        new_array = self.make_array(self.capacity)
        for x in range(i):
            new_array[x] = self.array[x]
        for x in range(i+1,self.count):
            new_array[x-1] = self.array[x]

        self.array = new_array

        self.count = self.count - 1
    

