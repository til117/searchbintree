from queue import Queue
from bintree import BinTree
import sys

fil=open("word3", encoding="latin-1")
ord=fil.readlines()
ordträd=BinTree()
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
    if son==None:
        return sonChain
    else:
        writeChain2(son.father,sonChain) #anropar sig själv med fadern som huvudparameter
        sonChain.append(son.word) #lägger in det i sonchain listan

def makeSons(startord):
    for n in range(0,3): 
        startordlista=[]
        for k in startord.word: 
            startordlista.append(k) 
        for bokstav in alfabetet:
            output=""
            startordlista[n]=bokstav
            for m in startordlista: #skapar ett ord
                output+=m
            if not oldwords.exists(output) and ordträd.exists(output): 
                oldwords.put(output)
                outputNode=Node(output) #skapar två noder, sonen pekar till fadern..
                outputNode.father=startord
                q.put(outputNode) #lägger noderna i kön
                if(output==slutord):
                    chain=writeChain(outputNode)
                    print(chain) #hittar vi slutordet så skapar vi en lista av writechain sen stänger vi av programmet.
                    sys.exit(0)

startord=Node(input("Skriv ett startord:"))
oldwords.put(startord.word)
slutord=input("Skriv ett slutord:")
q.put(startord)
while not q.isempty():
    makeSons(q.get())
print("Det finns ingen väg!")
