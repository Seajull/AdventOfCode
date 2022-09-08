import sys, re
def partOne(inpu,rep) :
    with open(inpu,'r') as inp :
        line=0
        mat=[]
        c=0
        for i in inp :
            if line==0 : 
                iea=i[:-1]
            elif line > 1 :
                if not mat :
                    leni=len(i[:-1])
                    while c<rep*2 :
                        mat.append([])
                        mat[c]+=["."]*(leni+rep*4) 
                        c+=1
                mat.append([])
                mat[line-2+(rep*2)]+=["."]*(rep*2)
                for j in i[:-1]:
                    mat[line-2+(rep*2)]+=[j]
                mat[line-2+(rep*2)]+=["."]*(rep*2)
            line+=1
        c=0
        while c<rep*2 :
            mat.append(["."]*(leni+rep*4))
            c+=1
#        for i in mat :
#            print("".join(i))
#        print()
        
        c=0 
        while c<rep :
            newmat=[]
            for i in mat :
                newmat.append(list(i))
            mat=enhance(mat,newmat,iea)
            c+=1
        count=0
        for i in mat :
            for j in i :
                if j=="#" :
                    count+=1
        return(count)
        

def enhance(mat,newmat,iea) :
    y=0
    while y<len(mat):
        x=0
        while x<len(mat[y]) :
            if y-1 < 0 or y+1>=len(mat) or x-1 < 0 or x+1>=len(mat[y]) :
                if mat[y][x] == "." :
                    newmat[y][x]=iea[0]
                else :
                    newmat[y][x]=iea[-1]
            else :
                bina=mat[y-1][x-1:x+2]
                bina+=mat[y][x-1:x+2]
                bina+=mat[y+1][x-1:x+2]
                bina=["0" if x=="."  else "1" if x=='#' else x for x in bina]
                bina="".join(bina)
                bina=int(bina,2)
                newmat[y][x]=iea[bina]
            x+=1
        y+=1

#    for i in newmat :
#        print("".join(i))
    return(newmat)
    
            






print()
print("==> PART ONE <==")
print()
print(partOne(sys.argv[1],2))

##############################################################################

def partTwo(inpu,rep) :
    with open(inpu,'r') as inp :
        line=0
        mat=[]
        c=0
        for i in inp :
            if line==0 : 
                iea=i[:-1]
            elif line > 1 :
                if not mat :
                    leni=len(i[:-1])
                    while c<rep*2 :
                        mat.append([])
                        mat[c]+=["."]*(leni+rep*4) 
                        c+=1
                mat.append([])
                mat[line-2+(rep*2)]+=["."]*(rep*2)
                for j in i[:-1]:
                    mat[line-2+(rep*2)]+=[j]
                mat[line-2+(rep*2)]+=["."]*(rep*2)
            line+=1
        c=0
        while c<rep*2 :
            mat.append(["."]*(leni+rep*4))
            c+=1
#        for i in mat :
#            print("".join(i))
#        print()
        
        c=0 
        while c<rep :
            newmat=[]
            for i in mat :
                newmat.append(list(i))
            mat=enhance(mat,newmat,iea)
            c+=1
        count=0
        for i in mat :
            for j in i :
                if j=="#" :
                    count+=1
        return(count)
        

def enhance(mat,newmat,iea) :
    y=0
    while y<len(mat):
        x=0
        while x<len(mat[y]) :
            if y-1 < 0 or y+1>=len(mat) or x-1 < 0 or x+1>=len(mat[y]) :
                if mat[y][x] == "." :
                    newmat[y][x]=iea[0]
                else :
                    newmat[y][x]=iea[-1]
            else :
                bina=mat[y-1][x-1:x+2]
                bina+=mat[y][x-1:x+2]
                bina+=mat[y+1][x-1:x+2]
                bina=["0" if x=="."  else "1" if x=='#' else x for x in bina]
                bina="".join(bina)
                bina=int(bina,2)
                newmat[y][x]=iea[bina]
            x+=1
        y+=1

#    for i in newmat :
#        print("".join(i))
    return(newmat)


print()
print("==> PART TWO <==")
print()
print(partTwo(sys.argv[1],50))
print()


