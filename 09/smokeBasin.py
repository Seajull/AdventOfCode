import sys, re

def partOne(inpu) :
    with open(inpu,'r') as inp :
        riskLevel=0
        hmap=[]
        for i in inp :
            hmap.append([int(j) for j in i[:-1]])
        c=0
        while c<len(hmap) :
            k=0
            while k<len(hmap[c]):
                riskLevel+=infVoisin([c,k],hmap)
                k+=1
            c+=1
    return(riskLevel)

def infVoisin(pos,hmap) :
    """
    pos is a list of coord [x,y]
    limit is a list of coord defining the top and bottom [nbrLine,nbrColonne]
    """
    x=pos[0]
    y=pos[1]
    if x==0 :
        up=10
    else :
        up=hmap[x-1][y]
    if x+1==len(hmap) :
        down=10
    else:
        down=hmap[x+1][y]
    if y==0 :
        left=10
    else :
        left=hmap[x][y-1]
    if y+1==len(hmap[x]):
        right=10
    else :
        right=hmap[x][y+1]
    if hmap[x][y]<up and hmap[x][y]<down and hmap[x][y]<left and hmap[x][y]<right :
        return(hmap[pos[0]][pos[1]]+1)
    else :
        return(0)
    

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        hmap=[]
        for i in inp :
            hmap.append([int(j) for j in i[:-1]])
        c=0
        firl=[]
        while c<len(hmap) :
            k=0
            while k<len(hmap[c]):
                voi=getInfVoisin([c,k],hmap)
                if voi :
                    firl.append(voi)
                k+=1
            c+=1
        bassin=[]
        flooded=[]
        i=0
        while i<len(firl) :
            bassin.append([])
            bassin[i].append(getVoisin([firl[i]],hmap,i))
            i+=1
    sizeBa=[]
    for i in bassin :
        sizeBa.append(len(i[0]))
    sizeBa.sort()
    return(sizeBa[-3]*sizeBa[-2]*sizeBa[-1])
        
def getInfVoisin(pos,hmap) :
    """
    pos is a list 2of coord [x,y]
    """
    x=pos[0]
    y=pos[1]
    coords=[]
    if x==0 :
        up=10
    else :
        up=hmap[x-1][y]
        coords.append([x-1,y])
    if x+1==len(hmap) :
        down=10
    else:
        down=hmap[x+1][y]
        coords.append([x+1,y])
    if y==0 :
        left=10
    else :
        left=hmap[x][y-1]
        coords.append([x,y-1])
    if y+1==len(hmap[x]):
        right=10
    else :
        right=hmap[x][y+1]
        coords.append([x,y+1])
    if hmap[x][y]<up and hmap[x][y]<down and hmap[x][y]<left and hmap[x][y]<right :
        coords=[i for i in coords if hmap[i[0]][i[1]]!=9]    
        return(pos)

def getVoisin(pos,hmap,ind,bas=None):
    if not bas :
        bas=[]
    found=False
    lol=[]
    for i in pos :
        x=i[0]
        y=i[1]
        coords=[]
        if i not in bas :
            lol.append(i)
        if not x==0 :
            coords.append([x-1,y])
        if not x+1==len(hmap) :
            coords.append([x+1,y])
        if not y==0 :
            coords.append([x,y-1])
        if not y+1==len(hmap[x]):
            coords.append([x,y+1])
        for j in coords :
            if not hmap[j[0]][j[1]]==9 :
                if j not in bas:
                    found=True
                    bas.append(j)
                    lol.append(j)
    if found :
        return(getVoisin(lol,hmap,ind,bas))
    else :
        return(bas)
        





print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()



def partTwoHorrible(inpu) :
    with open(inpu,'r') as inp :
        hmap=[]
        for i in inp :
            hmap.append([int(j) for j in i[:-1]])
        c=0
        bassin=[]
        while c<len(hmap) :
            bassin.append([])
            k=0
            rec=False
            found=False
            while k<len(hmap[c]):
                last=hmap[c][k]
                if not rec and hmap[c][k]!=9 :
                    rec=True
                    start=k
                if rec and hmap[c][k]==9 :
                    rec=False
                    end=k-1
                    bassin[c].append([start,end])
                k+=1
            if last!=9 :
                end=k-1
                bassin[c].append([start,end])
            c+=1
        c=0
        cluster=[]
        found=[]
        notFound=False
        print(bassin)
        while c<len(bassin):
            if c==0 :
                for i in bassin[c]:
                    cluster.append([[[i[0],i[1]]],i[1]-i[0]+1,c])
                print(cluster)
                c+=1
                continue
            for i in bassin[c]:
                j=0
                while j<len(cluster):
                    for n in cluster[j][0] :
                        if i[0]<=n[1] and i[1]>=n[0] and c==cluster[j][2]+1:
#                        cluster[j]=[i[0],i[1],cluster[j][2]+i[1]-i[0]+1,c-1]
                            found.append([j,i[0],i[1],i[1]-i[0]+1,c])
                            notFound=False
                            break
                        notFound=True
                    j+=1
                if notFound :
                    cluster.append([[[i[0],i[1]]],i[1]-i[0]+1,c])
                    notFound=False
            if found :
                print()
                print("FOUDN")
                print(found)
                for k in found : 
                    print("CLUSTER")
                    print(cluster)
                    cluster[k[0]]=[[]]+[cluster[k[0]][-2]+k[-2]]+[k[-1]]
                    cluster[k[0]][0].append([k[1],k[2]])
                    print("CLUSTER MOD")
                    print(cluster)
                found=[]
            c+=1
        size=[]
        for i in cluster :
            print(i)
            size.append(i[-2])
        size.sort()
        print(size[-3]*size[-2]*size[-1])


