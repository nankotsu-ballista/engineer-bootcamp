N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
left=0
right=10000000001
count=0
Acount=0
Bcount=0
AL=len(A)
BL=len(B)
while left <= right:
    Acount=0
    Bcount=0
    next = (left+right)//2
    for i in range(AL):
        if A[i]<=next:
            Acount+=1
            
    for i in range(BL):
        if B[i]>=next:
            Bcount+=1
    if Acount < Bcount:
        left = next+1
    else:
        ans=next
        right = next-1
    #count+=1
    #print(next)
    #print(Acount)
    #print(Bcount)
    #if Acount==Bcount:
       # print(count)
        #print(next)
    #if count==40:
       # print(count)
        #print(next)
        #exit()

Acount=0
Bcount=0

#for i in range(AL):
#    if A[i]<=next:
#        Acount+=1
            
#for i in range(BL):
#    if B[i]>=next:
#        Bcount+=1
#
#print(Acount)
#print(Bcount)
#print(left)
#genmax=-1
#for i in range(AL):
 #   if A[i]<=left and genmax<=A[i]:
 #           genmax=A[i]
print(ans)
        
