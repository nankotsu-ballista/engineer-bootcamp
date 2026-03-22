n,kk=map(int,input().split())
A=list(map(int,input().split()))
visited=[-1]*(n+1)
idx=0
ans=0
end=-1
k=kk
for i in range(kk):
    ans+=A[ans%n]
    if visited[idx]!=-1:
        them=visited[idx]
        end=i
        k-=1
        break
    visited[idx]=(i,ans)
    idx=ans%n
    k-=1
if i==kk-1:
    print(ans)
    exit()
#print(visited)
#print(end)
#print(them)
shou=k//(end-them[0])
amari=k%(end-them[0])
#print(shou,amari)
ans+=shou*(ans-them[1])
for i in range(amari):
    ans+=A[ans%n]
print(ans)
#print(826617499998784056-826617499999717503)