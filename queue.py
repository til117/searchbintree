class Node(object):
    def __init__(self, v):
        self.value=v
        self.next=None

class Queue(object):
    def __init__(self):
        self.__first=None
        self.__last=None

    def isempty(self):
        if(self.__first==None):
            return True
        return False

    def put(self, x):
        newNode=Node(x)
        if self.isempty():
            self.__first=newNode
            self.__last=newNode
        else:
            self.__last.next=newNode
            self.__last=self.__last.next

    def get(self):
        tmp=self.__first
        self.__first=self.__first.next
        return tmp.value

     
