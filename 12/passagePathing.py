import sys, re
def partOne(inpu) :
    dcon={}
    with open(inpu,'r') as inp :
        for i in inp :
            isp=i[:-1].split("-")
            if isp[0] in dcon.keys() :
                dcon[isp[0]].append(isp[1])
            else :
                dcon[isp[0]]=[isp[1]]
            if isp[1] in dcon.keys() :
                dcon[isp[1]].append(isp[0])
            else :
                dcon[isp[1]]=[isp[0]]
        pat=nextP(dcon,"start")
        patUni=[]
        for i in pat :
            if i not in patUni :
                patUni.append(i)
        return(len(patUni))


def nextP(dcon,node,lpath=[]) :
#    print(node)
#    print(dcon[node])
#    print()
    newpath=[]
    lpath=lpath+[node]
    if node=="end" :
        return [lpath]
    paths=[]
    for i in dcon[node] :
        if i.islower() and i not in lpath :
            newpath=nextP(dcon,i,lpath)
        if i.isupper() :
            newpath=nextP(dcon,i,lpath)
        for i in newpath :
            paths.append(i)
    return paths




print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))

##############################################################################

def partTwo(inpu) :
    dcon={}
    with open(inpu,'r') as inp :
        for i in inp :
            isp=i[:-1].split("-")
            if isp[0] in dcon.keys() :
                dcon[isp[0]].append(isp[1])
            else :
                dcon[isp[0]]=[isp[1]]
            if isp[1] in dcon.keys() :
                dcon[isp[1]].append(isp[0])
            else :
                dcon[isp[1]]=[isp[0]]
        pat=nextP2(dcon,"start")
        patUni=[]
        for i in pat :
            if i not in patUni :
                patUni.append(i)
        for i in patUni :
            if i[2]=="b" :
                continue
                print(i)
                print()
        return(len(patUni))


def nextP2(dcon,node,lpath=[]) :
#    print(node)
#    print(dcon[node])
#    print()
    newpath=[]
    lpath=lpath+[node]
    c=0
    ll=[]
    for i in lpath :
        if i.islower() and i not in ll :
            ll.append(i)
        elif i.islower() and i in ll :
            c+=1
    if c>1 :
        return None
    if node=="end" :
        return [lpath]
    paths=[]
    for i in dcon[node] :
        if i.islower() and i != "start":
            newpath=nextP2(dcon,i,lpath)
        if i.isupper() :
            newpath=nextP2(dcon,i,lpath)
        if newpath :
            for i in newpath :
                paths.append(i)
    return paths



print()
print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()


