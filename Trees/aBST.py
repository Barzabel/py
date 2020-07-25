

class aBST:

    def __init__(self, depth):

        tree_size =0
        for x in range(depth+1):
            tree_size = tree_size + (2**x)


        self.Tree = [None] * tree_size  # массив ключей
        self.void = True

    def FindKeyIndex(self, key):
        i = 0
        while i<len(self.Tree):
            if self.Tree[i]==None and i ==0:
                return 0
            if self.Tree[i] == None:

                return -i
            if self.Tree[i] == key:
                return i
            elif self.Tree[i] != key and self.Tree[i]!=None:

                if self.Tree[i]>key:
                    i = 2 * i + 1
                elif self.Tree[i]<key:
                    i = 2 * i + 2

        return None  # не найден

    def AddKey(self, key):
        if self.void:
            self.Tree[0]=key
            self.void = False
            return 0
        i = self.FindKeyIndex(key)
        if i == None:
            return -1
        if i >=0 :
            return i


        if i <0 :
            self.Tree[-i]=key
            return -i





        # индекс добавленного/существующего ключа или -1 если не удалось




















