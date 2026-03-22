n=int(input())
A=list(map(int,input().split()))
numbers=[]
i=0
while i<n-1:
    count=0
    d=A[i+1]-A[i]
    j=i
    while j<n-1 and A[j+1]-A[j]==d:
        j+=1
        count+=1
    numbers.append(count)
    i+=count
zerosum=0
for i in range(len(numbers)):
    zerosum+=((numbers[i]+1)*numbers[i]//2)
print(zerosum+n)
        