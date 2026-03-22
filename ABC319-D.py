def gyou(a):
    sum=0
    gyousuu=1
    mojisuu=0
    for i in range(count):
        if sum +L[i] +mojisuu >a:
            gyousuu +=1
            sum =L[i]
            mojisuu = 1
        else:
            sum+=L[i]
            mojisuu +=1
    if gyousuu>M :
        return False
    if gyousuu==M and sum>a:
        return False
    else:
        return True
    
        
        
        
    

N,M= map(int,(input().split()))
L=list(map(int,input().split()))
count=len(L)
inf=10**18
left=max(L)
right=inf
while right>left:
    mid=(right+left)//2
    if gyou(mid)==True:
        right=mid
    else:
        left=mid+1
print(left)
