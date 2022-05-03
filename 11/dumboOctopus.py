import sys, re
nbrFlash=0
def partOne(inpu,step) :
    with open(inpu,'r') as inp :
        mapOcto=[[int(j) for j in i[:-1]] for i in inp] # it work trust me
#        print("---------------------------------")
#        for i in mapOcto:
#            print(i)
        c=0
        while c<step :
            up(mapOcto)
            c+=1

def up(mapo) :
    l=0
    alert=False
    while l<len(mapo):
        p=0
        while p<len(mapo[l]) :
            mapo[l][p]+=1
            if mapo[l][p]==10 :
                alert=True
            p+=1
        l+=1
    if alert :
        mapo=flash(mapo)
#        print("NEXT STEP")
#    print("---------------------------------")
#    for i in mapo:
#        print(i)

def flash(mapo) :
    global nbrFlash
    l=0
    flas=False
    while l<len(mapo):
        p=0
        while p<len(mapo[l]) :
            if type(mapo[l][p])==int :
                if mapo[l][p]>=10 :
                    mapo[l][p]="f"
                    try :
                        if p-1>=0 and l-1>=0 :
                            mapo[l-1][p-1]+=1
                    except: 
                        pass
                    try :
                        if l-1>=0 :
                            mapo[l-1][p]+=1
                    except: 
                        pass
                    try :
                        if l-1>=0 :
                            mapo[l-1][p+1]+=1
                    except: 
                        pass
                    try :
                        if p-1>=0 :
                            mapo[l][p-1]+=1
                    except: 
                        pass
                    try :
                        mapo[l][p+1]+=1
                    except: 
                        pass
                    try :
                        if p-1>=0 :
                            mapo[l+1][p-1]+=1
                    except: 
                        pass
                    try :
                        mapo[l+1][p]+=1
                    except: 
                        pass
                    try :
                        mapo[l+1][p+1]+=1
                    except: 
                        pass
                    flas=True
                    break
                else :
                    flas=False
            p+=1
        if flas :
            break
        l+=1
    if flas :
        nbrFlash+=1
        mapo=flash(mapo)
    else :
        l=0
        while l<len(mapo):
            p=0
            while p<len(mapo[l]) :
                if type(mapo[l][p])!=int :
                    mapo[l][p]=0
                p+=1
            l+=1
    return(mapo)
        


print()
print("==> PART ONE <==")
partOne(sys.argv[1],100)
print(nbrFlash)
print()

##############################################################################

def partTwo(inpu,step) :
    with open(inpu,'r') as inp :
        mapOcto=[[int(j) for j in i[:-1]] for i in inp] # it work trust me
#        print("---------------------------------")
#        for i in mapOcto:
#            print(i)
        global c
        c=0
        while c<step :
            up(mapOcto)
            c+=1

def up(mapo) :
    l=0
    alert=False
    while l<len(mapo):
        p=0
        while p<len(mapo[l]) :
            mapo[l][p]+=1
            if mapo[l][p]==10 :
                alert=True
            p+=1
        l+=1
    if alert :
        mapo=flash(mapo)
#        print("NEXT STEP")
#    print("---------------------------------")
#    for i in mapo:
#        print(i)

def flash(mapo) :
    l=0
    flas=False
    while l<len(mapo):
        p=0
        while p<len(mapo[l]) :
            if type(mapo[l][p])==int :
                if mapo[l][p]>=10 :
                    mapo[l][p]="f"
                    try :
                        if p-1>=0 and l-1>=0 :
                            mapo[l-1][p-1]+=1
                    except: 
                        pass
                    try :
                        if l-1>=0 :
                            mapo[l-1][p]+=1
                    except: 
                        pass
                    try :
                        if l-1>=0 :
                            mapo[l-1][p+1]+=1
                    except: 
                        pass
                    try :
                        if p-1>=0 :
                            mapo[l][p-1]+=1
                    except: 
                        pass
                    try :
                        mapo[l][p+1]+=1
                    except: 
                        pass
                    try :
                        if p-1>=0 :
                            mapo[l+1][p-1]+=1
                    except: 
                        pass
                    try :
                        mapo[l+1][p]+=1
                    except: 
                        pass
                    try :
                        mapo[l+1][p+1]+=1
                    except: 
                        pass
                    flas=True
                    break
                else :
                    flas=False
            p+=1
        if flas :
            break
        l+=1
    if flas :
        mapo=flash(mapo)
    else :
        nbrEle=sum(len(v) for v in mapo)
        countf=0
        l=0
        while l<len(mapo):
            p=0
            while p<len(mapo[l]) :
                if type(mapo[l][p])!=int :
                    mapo[l][p]=0
                    countf+=1
                p+=1
            l+=1
        if countf==nbrEle :
            print(c)
    return(mapo)

print("==> PART TWO <==")
partTwo(sys.argv[1],280)
print()


