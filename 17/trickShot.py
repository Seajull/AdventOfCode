import sys, re
def partOne(inpu) :
    with open(inpu,'r') as inp :
        for i in inp :
            res=re.search("x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)",i)
            if res :
                x=(int(res.group(1)),int(res.group(2)))
                y=(int(res.group(3)),int(res.group(4)))
    n=x[0]
    c=0
    som=0
    while som<n :
        c+=1
        som+=c
    velocity=[c,(y[0]*-1)-1] 
    m=velocity[1]    
    som=0
    while m>0 :
        som+=m
        m-=1
    return(som)

print()
print("==> PART ONE <==")
print()
print(partOne(sys.argv[1]))

##############################################################################

from itertools import product

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        for i in inp :
            res=re.search("x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)",i)
            if res :
                x=(int(res.group(1)),int(res.group(2)))
                y=(int(res.group(3)),int(res.group(4)))
    x2=x[1]
    list_x=[]
    n=x[0]
    c=0
    som=0
    while som<n :
        c+=1
        som+=c
    x1=c
    while x1<=x2 :
        list_x.append(x1)
        x1+=1
    ymax=(y[0]*-1)-1
    ymin=y[0]
    list_y=[]
    while ymin<ymax :
        list_y.append(ymin)
        ymin+=1
        
    list_y.append((y[0]*-1)-1)
    true_x=[]
    for i in list_x : 
        if x[0] <= i <= x[1] :
            true_x.append(i)
            continue
        c=i
        j=i
        while not x[0] <= i <= x[1] :
            c-=1
            i=i+c
            if i > x[1] :
                break

        if x[0] <= i <= x[1] :
            true_x.append(j)
    ok_coords=[]
    true_xfiter=[]
    for j in true_x :
        miny=y[0]
        if x[0] <= j <= x[1]:
            while miny != y[1]+1 :
                ok_coords.append((j,miny))
                miny+=1
        else :
            true_xfiter.append(j)
    true_x=true_xfiter
    true_y=[]
    for i in list_y :
        if not y[0] <= i <= y[1]:
            true_y.append(i)
    for i in true_x :
        for j in true_y :
            coord=(i,j)
            cox=coord[0]
            coy=coord[1]
            xp=coord[0]
            yp=coord[1]
            while xp <= x[1] and yp >= y[0] :
                if cox > 0 :
                    cox-=1
                elif cox < 0 :
                    cox+=1
                coy-=1
                if x[0] <= xp <= x[1] and y[0] <= yp <= y[1]:
                    ok_coords.append(coord)
                    break
                else : 
                    xp+=cox
                    yp+=coy
    return(len(ok_coords))

            
            


print()
print("==> PART TWO <==")
print()
print(partTwo(sys.argv[1]))
print()


