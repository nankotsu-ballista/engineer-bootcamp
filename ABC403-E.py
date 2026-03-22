from collections import defaultdict
q=int(input())
triex=[[-1]*(26)]
#print(triex)
xcount=1
ans=0
names=[set() for _ in range(10**6+1)]
Scount=defaultdict(int)
endx=set()
X=set()
Y=set()
Z=set()

for que in range(q):
    t,s=map(str,input().split())
    Scount[s]+=1
    S=s
    s=list(s)
    if t=="1":
        X.add(S)
        point=0
        for i in range(len(s)):
            if triex[point][ord(s[i])-97]==-1:
                triex[point][ord(s[i])-97]=xcount
                triex.append([-1]*(27))
                point=xcount
                xcount+=1
            elif triex[point][ord(s[i])-97]!=-1:
                point=triex[point][ord(s[i])-97]
        endx.add(point)
        #その点にあるYの要素を全消し
        for i in names[point]:
            Z.add(i)
        names[point]=set()
    elif t=="2":
        point=0
        check=False
        for i in range(len(s)):
            if triex[point][ord(s[i])-97]==-1:
                triex[point][ord(s[i])-97]=xcount
                triex.append([-1]*(27))
                point=xcount
                xcount+=1
                names[point].add(que)
                if point in endx:
                    check=True
            elif triex[point][ord(s[i])-97]!=-1:
                point=triex[point][ord(s[i])-97]
                names[point].add(que)
                if point in endx:
                    check=True
        if check==True:
            Z.add(que)
        Y.add(que)
            
    print(len(Y)-len(Z))
            

#print(point)
    

# print(names[:15])
# for i in triex:
#     print(i)
# print()

# print(X)
# print(Y)
# print(Z)






