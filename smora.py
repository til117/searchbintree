from queue import Queue
from bintree import BinTree

fil=open("word3", encoding="latin-1")
ord=fil.readlines()
ordträd=BinTree()
godlist=[]
oldwords=BinTree()
for n in ord:
    ordträd.put(n.rstrip("\n"))

alfabetet='abcdefghijklmnopqrstuvwxyzåäö'

q=Queue()

class Node(object):
    def __init__(self,w):
        self.word=w
        self.father=None

def writeChain(son):
    sonChain=[]
    writeChain2(son,sonChain)
    return sonChain


def writeChain2(son,sonChain):
    if son.father==None:
        sonChain.append(son.word)
        return sonChain
    else:
        writeChain2(son.father,sonChain)
        sonChain.append(son.word)

def makeSons(startord):
    output=""
    for n in range(0,3):
        startordlista=[]
        for k in startord.word:
            startordlista.append(k)
        for bokstav in alfabetet:
            output=""
            startordlista[n]=bokstav
            for m in startordlista:
                output+=m
            if not oldwords.exists(output) and ordträd.exists(output):
                oldwords.put(output)
                outputNode=Node(output)
                outputNode.father=startord
                q.put(outputNode)
                chain=writeChain(outputNode)
                godlist.append(chain)
#                print(chain)


startord=Node(input("Write a starting word:"))
oldwords.put(startord.word)
q.put(startord)
while not q.isempty():
    makeSons(q.get())

print("\n\nLongest list:",godlist[len(godlist)-1],"\n\nTotal number of words between the first and the last word:",len(godlist[len(godlist)-1])-2)
