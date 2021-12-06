import sys, re

def partOne(inpu) :
    with open(inpu,'r') as inp :
        totList=[]
        for i in inp :
            for j in i[:-1] :
                totList.append([0,0])
            break
        inp.seek(0)
        for i in inp :
            count=0
            for j in i[:-1] :
                if j=="0":
                    totList[count][0]+=1
                else :
                    totList[count][1]+=1
                count+=1
    gamma=""
    epsilon=""
    for i in totList :
        gamma+=str(i.index(max(i)))
        epsilon+=str(i.index(min(i)))
    return(int(gamma,2)*int(epsilon,2))

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        totI=[]
        for i in inp :
            totI.append(i[:-1])
        def rating(bit,totI,typ) :
            lis=[0,0]
            for i in totI :
                if i[bit]=="0" :
                    lis[0]+=1
                else :
                    lis[1]+=1
            new=[]
            if lis[0]==lis[1] :
                for i in totI :
                    if typ=="oxygen" :
                        if i[bit]=="1":
                            new.append(i)
                    elif typ=="co2": 
                        if i[bit]=="0":
                            new.append(i)
            else :
                for i in totI :
                    if typ=="oxygen" :
                        if i[bit]==str(lis.index(max(lis))):
                            new.append(i)
                    elif typ=="co2": 
                        if i[bit]==str(lis.index(min(lis))):
                            new.append(i)
            if len(new)==1 :
                return(new[0])
            bit+=1
            return(rating(bit,new,typ))
        return(int(rating(0,totI,"oxygen"),2)*int(rating(0,totI,"co2"),2))

                


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()
