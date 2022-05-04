import sys, re
def partOne(inpu) :
    with open(inpu,'r') as inp :
        x=[]
        y=[]
        coord=[]
        fo=False
        fold=[]
        for i in inp : 
            if i=="\n": 
                fo=True
                continue
            if fo :
                res=re.search("along (\w)=(\d+)\n",i)
                fold.append((res.group(1),int(res.group(2))))
            else :
                isp=i[:-1].split(",")
                x.append(int(isp[0]))
                y.append(int(isp[1]))
                coord.append((int(isp[0]),int(isp[1])))
        tp=[ ["."]*(max(x)+1) for i in range(max(y)+1)]
        for i in coord :
            tp[i[1]][i[0]]="#"
#        for i in tp :
#            print(" ".join(i))
#        print()
        for i in fold :
            newcoord=[]
            if i[0]=="y" :
                newtp=tp[0:i[1]]
                for c in coord :
                    if c[1]>i[1] :
                        newcoord.append((c[0],abs(c[1]-max(y))))
            else :
                newtp=[]
                for lp in tp:
                    newtp.append(lp[0:i[1]])
                for c in coord :
                    if c[0]>=i[1] :
                        newcoord.append((abs(c[0]-max(x)),c[1]))
            break
        for i in newcoord :
            newtp[i[1]][i[0]]="#"
#        print('-------------------------------\n')
#        for i in newtp :
#            print(" ".join(i))
#        print()
        c=0
        for i in newtp :
            for j in i :
                if j=="#" :
                    c+=1
        return c





print()
print("==> PART ONE <==")
print()
print(partOne(sys.argv[1]))

##############################################################################

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        x=[]
        y=[]
        coord=[]
        fo=False
        fold=[]
        for i in inp : 
            if i=="\n": 
                fo=True
                continue
            if fo :
                res=re.search("along (\w)=(\d+)\n",i)
                fold.append((res.group(1),int(res.group(2))))
            else :
                isp=i[:-1].split(",")
                x.append(int(isp[0]))
                y.append(int(isp[1]))
                coord.append((int(isp[0]),int(isp[1])))
        tp=[ ["."]*(max(x)+1) for i in range(max(y)+1)]
        for i in coord :
            tp[i[1]][i[0]]="#"
        for i in tp :
            print(" ".join(i))
        print()
        print("------------")
        print()
        maxy=max(y)
        maxx=max(x)
        newtp=tp
        for i in fold :
            newcoord=[]
            if i[0]=="y" :
                newtp=newtp[0:i[1]]
                for c in coord :
                    if c[1]>i[1] :
                        newcoord.append((c[0],abs(c[1]-maxy)))
            else :
                oldtp=newtp
                newtp=[]
                for lp in oldtp:
                    newtp.append(lp[0:i[1]])
                for c in coord :
                    if c[0]>=i[1] :
                        newcoord.append((abs(c[0]-maxx),c[1]))
            for n in newcoord :
                newtp[n[1]][n[0]]="#"
            k=0
            coord=[]
            maxy=len(newtp)-1
            while k < len(newtp):
                m=0
                maxx=len(newtp[k])-1
                while m<len(newtp[k]) :
                    if newtp[k][m]=="#":
                        coord.append((m,k))
                    m+=1
                k+=1
            for r in newtp :
                print(" ".join(r))
            print()
            print("------------")
            print()

#        print('-------------------------------\n')
#        for i in newtp :
#            print(" ".join(i))
#        print()

print()
print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()


