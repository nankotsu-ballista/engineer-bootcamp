from sortedcontainers import SortedSet
        
n,q=map(int,input().split())
colorcount=[1]*(n+1)
leftside=SortedSet([])
blockcolor=[]
for i in range(n+1):
    leftside.add((i))
    blockcolor.append(i)
leftside.discard(0)
for i in range(q):
    A=list(map(int,input().split()))
    if A[0]==1:
        x=A[1]
        c=A[2]
        idx=leftside.bisect_right(x)-1
        # print(idx,leftside)
        before=blockcolor[leftside[idx]]
        #print(leftside.bisect_left(x))
        blockcolor[leftside[idx]]=c
        if idx==len(leftside)-1:
          colorcount[before]-=n+1-leftside[idx]
          colorcount[c]+=n+1-leftside[idx]
          blockcolor[leftside[idx]]=c
          if idx!=0:
            idx2=idx-1
            if blockcolor[leftside[idx]]==blockcolor[leftside[idx2]]:
              leftside.discard(leftside[idx])
        else:
          if idx!=len(leftside)-1:
            idx3=idx+1
            colorcount[before]-=leftside[idx3]-leftside[idx]
            colorcount[c]+=leftside[idx3]-leftside[idx]
            if blockcolor[leftside[idx3]]==blockcolor[leftside[idx]]:
              leftside.discard(leftside[idx3])
          if idx!=0:
            idx2=idx-1
            if blockcolor[leftside[idx2]]==blockcolor[leftside[idx]]:
              leftside.discard(leftside[idx])
         
        
    elif A[0]==2:
        c=A[1]
        print(colorcount[c])
#     print(before,c)
#     print(colorcount)   
# print(leftside)
# print(blockcolor)