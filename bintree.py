class BinNode(object):
    def __init__(self,v):
        self.value=v
        self.right=None
        self.left=None

class BinTree(object):
    def __init__(self):
        self.root=None

    def exists(self,value):
        return self.__finns(value, self.root)

    def __finns(self, value, r):
        while r!=None :
            if value < r.value:
                r = r.left
            elif value > r.value:
                r = r.right
            else:
                return True
        return False

    def put(self,value):
        self.root = self.__insert(value, self.root)


    def __insert(self, value, r):
        if r == None:
            r = BinNode(value)
            return r
        if value < r.value:
            r.left = self.__insert(value, r.left)
        elif value > r.value:
            r.right = self.__insert(value, r.right)
        else:
            print("Dubblett: " , value)
        return r

    def write(self):
        self.__skriv(self.root)
    
    def __skriv(self, r):
        if r == None:
            return
        self.__skriv(r.left)
        print(r.value)
        self.__skriv(r.right)

    def nElements(self):
        return self.__antalElementer(self.root)

    def __antalElementer(self,r):
        if r == None:
            return 0;
        return 1+self.__antalElementer(r.left)+self.__antalElementer(r.right);
