import sys, re

def partOne(inpu) :
    with open(inpu,'r') as inp :
        for i in inp :
            hexd=i[:-1]
    scale = 16 ## equals to hexadecimal
    num_of_bits = len(hexd)*4
    fullHex=bin(int(hexd, scale))[2:].zfill(num_of_bits)
    print(fullHex)
    print("--------------------------------------------------")
    print(parseHex(fullHex))
    


        
def parseHex(hexd,versionSum=0) : 
    versionSum+=int(hexd[0:3],2) 
    typeId=int(hexd[3:6],2)
 #    hexd="01010000001100100000100011000001100000"
    typeId=int(hexd[3:6],2)
    if typeId == 4 : 
        res=re.search("(1\d{4})?(0\d{4})",hexd[6:])
        prefix=hexd[0:6]
        if res :
            hexd=hexd.replace(prefix+res.group(0),"",1)
            print(hexd)
            return(hexd,versionSum)
        if not hexd :
            return(versionSum)

    if hexd[6] == "1": 
        numSub=int(hexd[7:18],2)
        subPackets=hexd[18:]
        lenSub=0

    elif hexd[6] == "0": 
        lenSub=int(hexd[7:22],2)
        subPackets=hexd[22:22+lenSub]
        numSub=0
        count=-1
        
    while len(hexd) >= 11 :
            hexd,versionSum=parseHex(subPackets,versionSum)
        
    return(versionSum)


#    if not found :
#        return(versionSum)


















print()
print("==> PART ONE <==")
print()
print(partOne(sys.argv[1]))

##############################################################################


def partTwo(inpu) :
    pass



print()
print("==> PART TWO <==")
print()
print(partTwo(sys.argv[1]))
print()


