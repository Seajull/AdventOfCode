import sys, re

def partOne(inpu) :
    with open(inpu,'r') as inp :
        overlap={}
        for i in inp :
            res=re.search("(\d+),(\d+) -> (\d+),(\d+)",i)
            if res :
                x1=int(res.group(1))
                y1=int(res.group(2))
                x2=int(res.group(3))
                y2=int(res.group(4))
            if x1==x2 :
                if y1<y2 :
                    start=y1
                    end=y2
                else :
                    start=y2
                    end=y1
                for j in range(start,end+1):
                    coord=(x1,j)
                    if str(coord) in overlap.keys() :
                        overlap[str(coord)]+=1
                    else :
                        overlap[str(coord)]=1
            if y1==y2 :
                if x1<x2 :
                    start=x1
                    end=x2
                else :
                    start=x2
                    end=x1
                for j in range(start,end+1):
                    coord=(j,y1)
                    if str(coord) in overlap.keys() :
                        overlap[str(coord)]+=1
                    else :
                        overlap[str(coord)]=1
    nbrOverlap=0
    for i in overlap.values() :
        if i>1 :
            nbrOverlap+=1
    return nbrOverlap

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        overlap={}
        for i in inp :
            res=re.search("(\d+),(\d+) -> (\d+),(\d+)",i)
            if res :
                x1=int(res.group(1))
                y1=int(res.group(2))
                x2=int(res.group(3))
                y2=int(res.group(4))
            if x1==x2 :
                if y1<y2 :
                    start=y1
                    end=y2
                else :
                    start=y2
                    end=y1
                for j in range(start,end+1):
                    coord=(x1,j)
                    if str(coord) in overlap.keys() :
                        overlap[str(coord)]+=1
                    else :
                        overlap[str(coord)]=1
            if y1==y2 :
                if x1<x2 :
                    start=x1
                    end=x2
                else :
                    start=x2
                    end=x1
                for j in range(start,end+1):
                    coord=(j,y1)
                    if str(coord) in overlap.keys() :
                        overlap[str(coord)]+=1
                    else :
                        overlap[str(coord)]=1
            if x1-x2==y1-y2 :
                if x1<x2 :
                    start=x1
                    end=x2
                else :
                    start=x2
                    end=x1
                y=min(y1,y2)
                for j in range(start,end+1):
                    coord=(j,y)
                    y+=1
                    if str(coord) in overlap.keys() :
                        overlap[str(coord)]+=1
                    else :
                        overlap[str(coord)]=1
            if x1+y1==x2+y2 :
                if x1<x2 :
                    start=x1
                    end=x2
                else :
                    start=x2
                    end=x1
                y=max(y1,y2)
                for j in range(start,end+1):
                    coord=(j,y)
                    y-=1
                    if str(coord) in overlap.keys() :
                        overlap[str(coord)]+=1
                    else :
                        overlap[str(coord)]=1
    nbrOverlap=0
    for i in overlap.values() :
        if i>1 :
            nbrOverlap+=1
    return nbrOverlap


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()
