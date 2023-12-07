import sys, re
def partOne(inpu,rep) :
    with open(inpu,'r') as inp :
        for i in inp :
            res1=re.search("Player 1 \w+ \w+: (\d+)",i)
            res2=re.search("Player 2 \w+ \w+: (\d+)",i)
            if res1 :
                p1=int(res1.group(1))
            elif res2 :
                p2=int(res2.group(1))
#        print(p1,p2)
        s1=0
        s2=0
        dice=[1,2,ver3]
        rolled=3
        while True :
            p1=int(str(p1+sum(dice))[-1])
            if p1==0 :
                p1=10
            s1+=p1
            if s1>=1000 :
                break
            dice=[x+3 if x+3 <= 100 else int(str(x+3)[-1]) for x in dice]
            rolled+=3
            p2=int(str(p2+sum(dice))[-1])
            if p2==0 :
                p2=10
            s2+=p2
            if s2>=1000 :
                break
            dice=[x+3 if x+3 <= 100 else int(str(x+3)[-1]) for x in dice]
            rolled+=3
        looser=min(s1,s2)
        return(looser*rolled)

print()
print("==> PART ONE <==")
print()
print(partOne(sys.argv[1],2))

##############################################################################

from functools import cache
def partTwo(inpu,rep) :
    with open(inpu,'r') as inp :
        for i in inp :
            res1=re.search("Player 1 \w+ \w+: (\d+)",i)
            res2=re.search("Player 2 \w+ \w+: (\d+)",i)
            if res1 :
                p1=int(res1.group(1))
            elif res2 :
                p2=int(res2.group(1))

def quantum(pos,jet,score=0,n_uni=0,dice=[1,2,3]) : 
    while score < 21 :









print()
print("==> PART TWO <==")
print()
print(partTwo(sys.argv[1],50))
print()



