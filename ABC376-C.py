from collections import defaultdict
n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
idx=21
check=False
for i in range(n-1):
    if B[i]<A[i]:
        idx=i
        check=True
        break
# print(A)
# print(B)
# print(n-idx)
if check==True:    
    for i in range(n-idx-1):
        #print(A[idx+i+1])
        #print(B[idx+i])
        #print(idx)
        if B[idx+i]>=A[idx+i+1]:
            continue
        else:
            print(-1)
            exit()
    print(A[idx])
else:
    print(A[n-1])
# print(A)
# print(B)
# print(idx)