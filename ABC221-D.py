from sortedcontainers import SortedList
n=int(input())
imos=SortedList([])
for i in range(n):
    a,b=map(int,input().split())
    imos.add((a,1))
    imos.add((a+b,-1))
sum=0
nowidx=0
ans=0
login=[0]*(n+1)
for i in imos:
  day,num=i
  login[sum]+=day-nowidx
  sum+=num
  nowidx=day
print(*login[1:])
  