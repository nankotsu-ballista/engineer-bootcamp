import bisect
n,q=map(int,input().split())
S=list(input())
onelist=[]
twolist=[]
slashlist=[]
ruiseki1=0
ruiseki2=0
for i in range(n):
    onelist.append(ruiseki1)
    twolist.append(ruiseki2)
    if S[i]=="1":
        ruiseki1+=1
    if S[i]=="2":
        ruiseki2+=1
    if S[i]=="/":
        slashlist.append(i)
onelist.append(ruiseki1)
twolist.append(ruiseki2)

# print(onelist)
# print(twolist)
# print(slashlist)

for i in range(q):
    l,r=map(int,input().split())
    L=bisect.bisect_left(slashlist,l-1)
    R=bisect.bisect_left(slashlist,r)
    if L==R:
        if l==r and S[l-1]=="/":
            print(1)
        else:
            print(0)
        continue
    ans=-1
    while L<R:
        mid=(L+R)//2
        slashidx=slashlist[mid]
        leftone=onelist[slashidx]-onelist[l-1]
        righttwo=twolist[r]-twolist[slashidx]
        ans=max(ans,2*(min(leftone,righttwo))+1)
        if leftone<righttwo:
            L=mid+1
        else:
            R=mid
    print(ans)
            