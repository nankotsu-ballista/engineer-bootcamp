n=int(input())
A=list(map(int,input().split()))
counter=[[0]*2 for _ in range(n+1)]
for i in A:
    counter[i][1]+=1
#print(counter)
sum=0
ans=0
for i in range(n):
    a=A[i]
    sum-=counter[a][0]*counter[a][1]
    counter[a][1]-=1
    counter[a][0]+=1
    ans+=sum
    sum+=counter[a][0]*counter[a][1]
    #print(sum)
print(ans)
    