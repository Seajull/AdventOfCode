import sys, re

"""
CURSED CODE ! DON'T POP OR REMOVE ITEM FROM LIST WHILE INTERATING IN IT !
(especially for partTwo)
"""

def partOne(inpu) :
    with open(inpu,'r') as inp :
        rea=False
        count=0
        listEmb=[]
        for i in inp :
            if not rea :
                rea=True
                listNbr=[int(j) for j in i[:-1].split(",")]
                continue
            if i[0]=="\n" :
                listEmb.append([])
                count+=1
                continue
            else :
                listEmb[count-1].append([int(j) for j in i[:-1].split(" ") if j!=""])
        fullList=[]
        for i in listEmb :
            col=list(map(list, zip(*i)))
            for j in col:
                i.append(j)
            fullList.append(i)
        bingo=False
        for i in listNbr :
            for ma in fullList :
                for j in ma :
                    if i in j :
                        j.remove(i)
                    if len(j)==0 :
                        bingo=True
                        winNbr=i
                        winMa=fullList.index(ma)
                        break
                if bingo :
                    break
            if bingo :
                break
        count=0
        tot=0
        for j in fullList[winMa] :
            if count<5 :
                for i in j :
                    tot+=i  
            count+=1
        return(tot*winNbr)



print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        rea=False
        count=0
        listEmb=[]
        for i in inp :
            if not rea :
                rea=True
                listNbr=[int(j) for j in i[:-1].split(",")]
                continue
            if i[0]=="\n" :
                listEmb.append([])
                count+=1
                continue
            else :
                listEmb[count-1].append([int(j) for j in i[:-1].split(" ") if j!=""])
        fullList=[]

        for i in listEmb :
            col=list(map(list, zip(*i)))
            for j in col:
                i.append(j)
            fullList.append(i)
        bingo=False
        i=0
        while i<len(listNbr) :
            for ma in fullList :
                for line in ma :
                    if listNbr[i] in line :
                        line.remove(listNbr[i])
                    if len(line)==0 :
                        bingo=True
                        break
                if bingo :
                    fullList.remove(ma)
                    winMa=ma
                    winNbr=listNbr[i]
                    break
            if bingo :
                bingo=False
            else :
                i+=1
        tot=0
        for i in winMa[0:5] :
            for j in i :
                tot+=j
        return(tot*winNbr)
                


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()
