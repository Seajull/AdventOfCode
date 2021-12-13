import sys, re

def partOne(inpu,step) :
    with open(inpu,'r') as inp :
        mapOcto=[i[:-1] for i in inp]
        c=0
        while c<step :
            flash(mapOcto)
            c+=1

def flash(mapo,pos=None,haveFlashed=None,nbrFlash=None) :
    if not haveFlashed :
        haveFlashed=[]
    if not nbrFlash :
        nbrFlash=0
    if not pos :
        pos=[[0,0]]
    newMapo=list(mapo)
    isFlash=False
    for i in pos :
        x=i[0]
        y=i[1]
        if int(mapo[x][y])>=9 :
            isFlash=True
            newMapo[x][y]=0
            nbrFlash+=1
            newPos=getVoisin([x,y],mapo)
            for j in newPos :
                newMapo[j[0]][j[1]]+=1
                flash(newMapo)
    if not isFlash :
        return(nbrFlash)

def getVoisin(pos,mapo):
    x=pos[0]
    y=pos[1]
    coords=[]
    if not x==0 :
        coords.append([x-1,y])
    if not y==0 :
        coords.append([x,y-1])
    if not y==0 and not x==0 :
        coords.append([x-1,y-1])
    if not x+1==len(hmap) :
        coords.append([x+1,y])
    if not y+1==len(hmap[x]):
        coords.append([x,y+1])
    if not x+1==len(hmap) and not y+1==len(hmap[x]):
        coords.append([x+1,y+1])
    if not y==0 and not x+1==len(hmap) :
        coords.append([x+1,y-1])
    if not x==0 and not y+1==len(hmap[x]):
        coords.append([x-1,y+1])
    return(coords)

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1],100))
print()

##############################################################################

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        pass

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()


