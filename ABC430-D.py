from sortedcontainers import SortedList
s = SortedList([])
n=int(input())
X=list(map(int,input().split()))
s.add(0)
s.add(X[0])
ans=2*(s[1]-s[0])
print(ans)
for i in range(1,n):
  s.add(X[i])
  #print(s)
  idx=s.index(X[i])
  range=0
  if  idx==0:
    #print("case1")
    if s[2]-s[1]>s[1]-s[0]:
      ans+=2*(s[1]-s[0])
      ans-=s[2]-s[1]
    else:
      ans+=s[1]-s[0]
  elif  idx==i+1:
    #print("case2")
    if s[idx]-s[idx-1]<s[idx-1]-s[idx-2]:
      ans+=2*(s[idx]-s[idx-1])
      ans-=s[idx-1]-s[idx-2]
    else:
      ans+=s[idx]-s[idx-1]
  else:
    #print("case3")
    L=10**18
    R=10**18
    if idx-2>-1:
      L=s[idx-1]-s[idx-2]
    if idx+1<len(s):
      R=s[idx+1]-s[idx-1]
    Lmin=min(L,R)
    newLmin=min(L,R,s[idx]-s[idx-1])
    ans-=Lmin
    ans+=newLmin
    L=10**18
    R=10**18
    if idx-1>-1:
      L=s[idx+1]-s[idx-1]
    if idx+2<len(s):
      R=s[idx+2]-s[idx+1]
    Rmin=min(L,R)
    newRmin=min(L,R,s[idx+1]-s[idx])
    ans-=Rmin
    ans+=newRmin
    ans+=min(s[idx+1]-s[idx],s[idx]-s[idx-1])
  print(ans)
    
    