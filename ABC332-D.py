from itertools import permutations
h,w=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(h)]
B=[list(map(int,input().split())) for _ in range(h)]
hh=[]
ww=[]
for i in range(h):
    hh.append(i)
for i in range(w):
    ww.append(i)
# print(A)
# print(B)
ans=10**18
for perm1 in permutations(hh):
    for perm2 in permutations(ww):
        tri=[[0]*w for _ in range(h)]
        for i in range(h):
            for k in range(w):
                tri[i][k]=B[perm1[i]][perm2[k]]
        check=0
        for i in range(h):
            if check==1:
                break
            for k in range(w):
                if tri[i][k]!=A[i][k]:
                    check=1
                    break
        if check==1:
            continue
        # print("Yes")
        # print(perm1)
        # print(perm2)
        tmpans=0
        for go in range(h):
            for goo in range(go+1,h):
                if perm1[goo]<perm1[go]:
                    tmpans+=1
        for go in range(w):
            for goo in range(go+1,w):
                if perm2[goo]<perm2[go]:
                    tmpans+=1
        ans=min(ans,tmpans)
if ans==10**18:
    print(-1)
else:
    print(ans)
