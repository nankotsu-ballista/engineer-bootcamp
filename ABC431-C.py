n,m,k=map(int,input().split())
H=list(map(int,input().split()))
B=list(map(int,input().split()))
H.sort()
B.sort()
# print(H)
# print(B)
bidx=0
hidx=0
count=0
while bidx<len(B) and hidx<len(H):
    if H[hidx]>B[bidx]:
        bidx+=1
    else:
        #print(hidx,bidx)
        bidx+=1
        hidx+=1
        count+=1
if count>=k:
    print("Yes")
else:
    print("No")