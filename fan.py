from bintree import BinTree
fil=open("word3", encoding="latin-1")
ord=fil.readlines()
ordträd=BinTree()
oldwords=BinTree()
for n in ord:
    ordträd.put(n.rstrip("\n"))

alfabetet='abcdefghijklmnopqrstuvwxyzåäö'

startord=input("Skriv ett startord:")
oldwords.put(startord)

def makeSons(startord):
     output=""
     for n in range(0,3):
        startordlista=[]
        for k in startord:
            startordlista.append(k)
        for bokstav in alfabetet:
            output=""
            startordlista[n]=bokstav
            for m in startordlista:
                output+=m
            if not oldwords.exists(output) and ordträd.exists(output):
                oldwords.put(output)
                print(output)

makeSons(startord)
print(oldwords.nElements())

