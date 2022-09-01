import sys, re
def partOne(inpu,step) :
    with open(inpu,'r') as inp :
        polyTemp=(inp.readline()[:-1])
        #print("Template:\t"+polyTemp)
        next(inp)
        comb={}
        for i in inp :
            isp=i[:-1].split(" -> " )
            comb[isp[0]]=isp[1]
        c1=0
        while c1<step :
            p1=0
            inter=[]
            while p1<len(polyTemp)-1 :
                inter.append(comb[polyTemp[p1]+polyTemp[p1+1]])
                p1+=1
            newpoly=""
            for i in zip(polyTemp,inter) :
                newpoly+=i[0]+i[1]
            newpoly=(newpoly+polyTemp[-1])
            polyTemp=newpoly
            #print()
            c1+=1
            #print("After step "+str(c1)+":\t"+newpoly)
        #print(newpoly.count(max(newpoly,key=newpoly.count)))
        #print(newpoly.count(min(newpoly,key=newpoly.count)))
        return(newpoly.count(max(newpoly,key=newpoly.count))-newpoly.count(min(newpoly,key=newpoly.count)))


print()
print("==> PART ONE <==")
print()
print(partOne(sys.argv[1],10))

##############################################################################

def partTwo(inpu,step) :
    with open(inpu,'r') as inp :
        polyTemp=(inp.readline()[:-1])
        #print("Template:\t"+polyTemp)
        next(inp)
        comb={}
        for i in inp :
            isp=i[:-1].split(" -> " )
            comb[isp[0]]=isp[1]
        polyTempStockage={}
        p1=0
        while p1<len(polyTemp)-1 :
            if polyTemp[p1]+polyTemp[p1+1] not in polyTempStockage.keys() :
                polyTempStockage[polyTemp[p1]+polyTemp[p1+1]]=1
            else :
                polyTempStockage[polyTemp[p1]+polyTemp[p1+1]]+=1
            p1+=1
        c1=0
        while c1<step :
            newsto={}
            for i in polyTempStockage:
                a=i[0]+comb[i]
                b=comb[i]+i[1]
                if a not in newsto :
                    newsto[a]=polyTempStockage[i]
                else :
                    newsto[a]+=polyTempStockage[i]
                if b not in newsto :
                    newsto[b]=polyTempStockage[i]
                else :
                    newsto[b]+=polyTempStockage[i]
            polyTempStockage=newsto
            c1+=1
        dcount={}
        for i in newsto:
            if i[0] not in dcount :
                dcount[i[0]]=newsto[i]
            else :
                dcount[i[0]]+=newsto[i]
            if i[1] not in dcount :
                dcount[i[1]]=newsto[i]
            else :
                dcount[i[1]]+=newsto[i]
        ma=dcount[polyTemp[0]]
        mi=dcount[polyTemp[0]]
        mal=""
        mil=""
        for i in dcount :
            if dcount[i]>ma :
                ma=dcount[i]
                mal=i
            if dcount[i]<mi :
                mi=dcount[i]
                mil=i
        return(round((ma+0.001)/2)-round((mi+0.001)/2))

        
print()
print("==> PART TWO <==")
print()
print(partTwo(sys.argv[1],40))
print()


