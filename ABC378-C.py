from collections import defaultdict
n=int(input())
A=list(map(int,input().split()))
idx=defaultdict(list)
B=[0]*n
for i in range(n):
    if idx[A[i]]:
        #print(idx[A[i]].pop())
        B[i]=idx[A[i]].pop()
    else:
        #print(-1)
        B[i]=-1
    idx[A[i]].append(i+1)
print(" ".join(str(x) for x in B))
    
