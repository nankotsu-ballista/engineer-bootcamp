n=int(input())
cards=[]
for i in range(n):
    a,c=map(int,input().split())
    cards.append((a,c,i))
    
cards.sort(key=lambda x:x[1])
v =0
ans=[]

for a,c,index in cards:
    if a > v:
        ans.append(index)
        v = a
ans.sort()
print(len(ans))
print(' '.join(str(x + 1) for x in ans))