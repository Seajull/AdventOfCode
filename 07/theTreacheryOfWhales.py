import sys, re

def partOne(inpu) :
    with open(inpu,'r') as inp :
        for i in inp :
            pos=[int(j) for j in i[:-1].split(",")]
            break
        tot=0
        for i in pos :
            tot+=i
        mean=int(tot/len(pos))
        maxi=max(pos)
        mini=min(pos)
        fullFuel=[]
        for point in range(mini,maxi+1) :
            fuel=[]
            for i in pos :
                fuel.append(abs(i-point))
            tot=0
            for i in fuel :
                tot+=i
            fullFuel.append(tot)
        return(min(fullFuel))

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        for i in inp :
            pos=[int(j) for j in i[:-1].split(",")]
            break
        tot=0
        for i in pos :
            tot+=i
        mean=int(tot/len(pos))
        maxi=max(pos)
        mini=min(pos)
        fullFuel=[]
        for point in range(mini,maxi+1) :
            fuel=[]
            for i in pos :
                fuel.append(abs(i-point)*((abs(i-point)+1)/2))
            tot=0
            for i in fuel :
                tot+=i
            fullFuel.append(tot)
        return(min(fullFuel))


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()
