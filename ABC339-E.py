n,d=map(int,input().split())
A=list(map(int,input().split()))
dp=[]
for i in range(2**20):
    dp.append(0)
dat=dp
#print(dat)
size = len(dat)
segment_tree=[0] * size * 2

for i in range(n):
    ans=-1
    left = max(0,A[i]-d)
    right = min(2**20,A[i]+d+1)
    left += size
    right += size
    while left <right:
        if left %2 !=0:
            ans =max(ans,segment_tree[left])
            left+=1
        if right %2 !=0:
            right-=1
            ans = max(ans,segment_tree[right])
        left //=2
        right //=2
    #segment_tree[A[i]+size]=ans+1
    
    
    idx=A[i]
    new_value=ans+1
    leaf = idx +size
    segment_tree[leaf]= new_value
    while leaf!=0:
        leaf//=2
        child1=segment_tree[leaf*2]
        child2=segment_tree[leaf*2+1]
        segment_tree[leaf] = max(child1, child2)
    #print(segment_tree,ans)
print(max(segment_tree))
    
