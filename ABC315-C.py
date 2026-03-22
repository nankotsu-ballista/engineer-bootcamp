from collections import deque

#N, M = map(int, input().split())
#S = input()
#C = list(map(int, input().split()))
def hantei(flav1,flav2,S1,S2):
    if flav1 != flav2:
        return S1+S2
    else:
        if S1 >= S2:
            return S1+S2//2
        else:
            return S2+S1//2
N = int(input())
max=0
maxposi=0
S=[0]*N
F=[0]*N
for i in range(N):
    f,s=map(int, input().split())
    S[i]=s
    F[i]=f
    if s >=max:
        max = s
        maxposi= i
        maxflev= f
#print(S)
#print(F)
        
ans = 0
for i in range(N):
    if i != maxposi:
        if ans<=hantei(maxflev,F[i],S[maxposi],S[i]):
            ans=hantei(maxflev,F[i],S[maxposi],S[i])
        #print(f)
       # print(F[i])
       # print("----")    
#ans=hantei()
print(ans)        
#print(maxflev)        
#print(maxposi)
#print(ans)
