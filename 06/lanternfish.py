import sys, re

def partOne(inpu,days) :
    with open(inpu,'r') as inp :
        for i in inp :
            startLan=[int(j) for j in i[:-1].split(",")]
            break
        for d in range(0,days) :
            listCo=[0]*8
            newLan=[]
            c=0
            new=0
            while c<len(startLan):
                if startLan[c]==0:
                    new+=1
                    newLan.append(6)
                else :
                    newLan.append(startLan[c]-1)
                c+=1
            for i in range(0,new):
                newLan.append(8)
            startLan=newLan
    return(len(startLan))


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1],80))
print()

def partTwo(inpu,days) :
    with open(inpu,'r') as inp :
        for i in inp :
            startLan=[int(j) for j in i[:-1].split(",")]
            break
        listCo=[0]*9
        for i in startLan:
            listCo[i]=listCo[i]+1
        d=0
        while d<days :
            listCo=listCo[1:-2]+[listCo[0]+listCo[-2]]+[listCo[-1]]+[listCo[0]]
            d+=1
    tot=0
    for i in listCo :
        tot+=i
    return(tot)


print("==> PART TWO <==")
print(partTwo(sys.argv[1],256))
print()
