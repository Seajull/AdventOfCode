import sys, re

def partOne(inpu) :
    with open(inpu,'r') as inp :
        wire=[0]*8
        for i in inp :
            isp=i[:-1].split(" | ")
            for j in isp[1].split(" "):
                wire[len(j)]+=1
    return(wire[2]+wire[4]+wire[3]+wire[7])


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

"""
GOOD IDEA, HORRIBLE CODE (compare number of difference between known and unknown pattern,
for example 4 and 9 have 2 diff while 4 have 4 diff with 0 and 6)
"""

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        config={0:"abcefg",1:"cf",2:"acdeg",3:"acdfg",4:"bcdf",5:"abdfg",6:"abdefg",7:"acf",8:"abcdefg",9:"abcdfg"}
        uni={2:1,4:4,3:7,7:8}
        for i in config:
            config[i]=[j for j in config[i]]
        tot=0
        for i in inp :
            isp=" ".join(i[:-1].split(" | ")).split(" ")
            is0=i[:-1].split(" | ")[0].split(" ")
            outVal=i[:-1].split(" | ")[1].split(" ")
            newConfig=dict(config)
            wire={}
            for j in is0:
                if len(j) not in wire.keys() :
                    wire[len(j)]=[j]
                else :
                    wire[len(j)].append(j)
                if len(j) in [2,4,3,7] :
                    newConfig[uni[len(j)]]=[n for n in j]
            for k in wire[6] :
                dif=set(newConfig[4])^set(k)
                if len(dif) == 2 :
                    newConfig[9]=[t for t in k]
                    wire[6].remove(k)
                    break
            for k in wire[5]:
                dif=set(newConfig[4])^set(k)
                if len(dif) == 5 :
                    newConfig[2]=[t for t in k]
                    wire[5].remove(k)
                    break
            for k in wire[5] :
                dif=set(newConfig[1])^set(k)
                if len(dif) == 3 :
                    newConfig[3]=[t for t in k]
                else :
                    newConfig[5]=[t for t in k] 
            for k in wire[6]:
                dif=set(newConfig[1])^set(k)
                if len(dif) == 4 :
                    newConfig[0]=[t for t in k]
                else :
                    newConfig[6]=[t for t in k] 
            strTot=""
            for j in outVal :
                c=0
                while c<10 :
                    dif=set(j)^set(newConfig[c])
                    if not dif :
                        strTot+=str(c)
                    c+=1
            tot+=int(strTot)
    return(tot)

        

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()
