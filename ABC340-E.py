n,m=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
c=1
while c<=n:
    c*=2
#print(c-len(A))
for i in range(c-len(A)):
    A.append(0)
dat=A
size = len(dat)
delay_segment_tree=[0] * size * 2
#print(dat)
for i in range(m):
    idx=B[i]+size
    sum=0
    while idx!=0:
        sum+=delay_segment_tree[idx]
        #print(idx)
        idx//=2
    sum+=A[B[i]]
    #print(sum)
    allplus=sum//n
    proceed=sum%n
    #print(allplus,proceed)
    delay_segment_tree[1]+=allplus
    A[B[i]]-=sum
    if B[i]+proceed+1<=n:
        left = B[i]+1
        right = B[i]+proceed+1
        left += size
        right += size
        count=3
        while left <right:
            if left %2 !=0:
                delay_segment_tree[left]+=1
                left+=1
            if right %2 !=0:
                right-=1
                delay_segment_tree[right]+=1
            left //=2
            right //=2
        #print(delay_segment_tree)
    else:
        left = B[i]+1
        right = n
        left += size
        right += size
        count=3
        while left <right:
            if left %2 !=0:
                delay_segment_tree[left]+=1
                left+=1
            if right %2 !=0:
                right-=1
                delay_segment_tree[right]+=1
            left //=2
            right //=2
            
        left = 0
        right = B[i]+proceed-n+1
        left += size
        right += size
        count=3
        while left <right:
            if left %2 !=0:
                delay_segment_tree[left]+=1
                left+=1
            if right %2 !=0:
                right-=1
                delay_segment_tree[right]+=1
            left //=2
            right //=2
        #print(delay_segment_tree)
answers=[]
for i in range(n):
    idx=i+size
    sum=0
    while idx!=0:
        sum+=delay_segment_tree[idx]
        idx//=2
    sum+=A[i]
    answers.append(sum)
print(*answers)





