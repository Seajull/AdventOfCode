import sys, re

def partOne(inpu) :
    with open(inpu,'r') as inp :
        f=0
        d=0
        for i in inp :
            res=re.search("\d+",i)
            if "forward" in i :
                f+=int(res.group(0))
            elif "up" in i :
                d-=int(res.group(0))
            else :
                d+=int(res.group(0))
    return(d*f)

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        f=0
        d=0
        a=0
        for i in inp :
            res=re.search("\d+",i)
            if "forward" in i :
                f+=int(res.group(0))
                d+=a*int(res.group(0))
            elif "up" in i :
                a-=int(res.group(0))
            else :
                a+=int(res.group(0))
    return(d*f)


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()
