import sys, re

def partOne(inpu) :
    with open(inpu,'r') as inp :
        op=["(","{","<","["]
        cl=[")","}",">","]"]
        sta=[]
        dico={")":3,"]":57,"}":1197,">":25137}
        tot=0
        for i in inp :
            sta=[]
            for j in i[:-1]:
                if j in op :
                    sta.append(j)
                else :
                    if sta[-1]==op[cl.index(j)]:
                        sta.pop(-1)
                    else :
                        tot+=dico[j]
                        break
    return(tot)

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

##############################################################################

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        op=["(","[","{","<"]
        cl=[")","]","}",">"]
        sta=[]
        dico={")":3,"]":57,"}":1197,">":25137}
        corrupt=False
        uncorrupt=[]
        for i in inp :
            sta=[]
            for j in i[:-1]:
                if j in op :
                    sta.append(j)
                else :
                    if sta[-1]==op[cl.index(j)] :
                        sta.pop(-1)
                    else:
                        corrupt=True
                        break
            if corrupt :
                corrupt=False
            else :
                uncorrupt.append([i[:-1],sta])
        compl=[]
        for i in uncorrupt :
            i[1].reverse()
            compl.append(i[1])
        listScore=[]
        for i in compl :
            score=0
            for j in i :
                score=score*5
                score+=op.index(j)+1
            listScore.append(score)
        listScore.sort()
        return(listScore[int(len(listScore)/2)])

                    


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()


