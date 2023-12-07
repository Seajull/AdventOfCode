import sys, re
def partOne(inpu) :
    mat=[]
    with open(inpu,'r') as inp :
        for i in inp :
            line=[]
            for j in i[:-1] : 
                l=[int(j),0]
                line.append(l)
            mat.append(line)
    cmax=len(mat)
    coord="0;0"
    voisin=getVoisin(coord,cmax)
    curC=0
    visited=[]
    updated={}
    visited.append(coord)
    print(mat)
    while len(visited) < sum([len(x) for x in mat]):
        for i in voisin :
            idV=str(i[0])+";"+str(i[1])
            if idV in visited :
                continue
            idVS=idV.split(";")
            cout=mat[int(idVS[0])][int(idVS[1])][0]
            curV=mat[int(idVS[0])][int(idVS[1])][1]
            if curV == 0 : 
                curV = cout+curC
            else : 
                curV = min(curV,curC+cout)
            mat[int(idVS[0])][int(idVS[1])][1]=curV
            updated[idV]=curV
        nex=min(updated.values())
        coord=get_key(nex,updated)
        updated.pop(coord)
        voisin=getVoisin(coord,cmax)
        visited.append(coord)
        coordS=coord.split(";")
        curC=mat[int(coordS[0])][int(coordS[1])][1]
    return mat[cmax-1][cmax-1][1]


def getVoisin(coord,cmax) :
    voisin=[]
    coord=coord.split(";")
    x=int(coord[0])
    y=int(coord[1])
    voisin.append((x+1,y))
    voisin.append((x-1,y))
    voisin.append((x,y+1))
    voisin.append((x,y-1))
    validateVoisin=[]
    for i in voisin :
        if not(-1 in i or cmax in i):
            validateVoisin.append(i)
    return(validateVoisin)
    
    
def get_key(val,dic):
    for key, value in dic.items():
        if val == value:
            return key
    return "key doesn't exist"

print()
print("==> PART ONE <==")
print()
print(partOne(sys.argv[1]))

##############################################################################
''' 
I hope you have time for this (~1h)
'''
def partTwo(inpu) :
    mat=[]
    with open(inpu,'r') as inp :
        for i in inp :
            line=[]
            for j in i[:-1] : 
                l=[int(j),0]
                line.append(l)
            mat.append(line)
    oldmat=list(mat)
    j=0
    while j<4 :
        newmat=[[[x[0]+1,x[1]] if x[0]+1<10 else [1,x[1]] for x in i] for i in oldmat]
        oldmat=list(newmat)
        i=0
        while i<len(newmat) :
            mat[i]+=newmat[i]
            i+=1
        j+=1
    j=0
    oldmat=list(mat)
    while j<4 :
        newmat=[[[x[0]+1,x[1]] if x[0]+1<10 else [1,x[1]] for x in i] for i in oldmat]
        oldmat=list(newmat)
        mat+=newmat
        j+=1
    cmax=len(mat)
    coord="0;0"
    voisin=getVoisin(coord,cmax)
    curC=0
    visited=[]
    updated={}
    visited.append(coord)
    while len(visited) < sum([len(x) for x in mat]):
        for i in voisin :
            idV=str(i[0])+";"+str(i[1])
            if idV in visited :
                continue
            idVS=idV.split(";")
            cout=mat[int(idVS[0])][int(idVS[1])][0]
            curV=mat[int(idVS[0])][int(idVS[1])][1]
            if curV == 0 : 
                curV = cout+curC
            else : 
                curV = min(curV,curC+cout)
            mat[int(idVS[0])][int(idVS[1])][1]=curV
            updated[idV]=curV
        nex=min(updated.values())
        coord=get_key(nex,updated)
        updated.pop(coord)
        voisin=getVoisin(coord,cmax)
        visited.append(coord)
        coordS=coord.split(";")
        curC=mat[int(coordS[0])][int(coordS[1])][1]
    return mat[cmax-1][cmax-1][1]



print()
print("==> PART TWO <==")
print()
#print(partTwo(sys.argv[1]))
print()


