import sys

def partOne(inpu) :
    with open(inpu,'r') as inp :
        mem=None
        count=0
        for i in inp :
            if not mem :
                mem=int(i[:-1])
                continue
            if int(i[:-1])>mem :
                count+=1
            mem=int(i[:-1])
    return(count)

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        mem=None
        count=0
        sumA=0
        listD=[]
        inc=0
        for i in inp :
            count+=1
            listD.append(int(i[:-1]))
            if count<3:
                continue
            sumA=sum(listD[count-3:count])
            if not mem :
                mem=sumA
                continue
            if sumA>mem:
                inc+=1
            mem=sumA
    return(inc)

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


