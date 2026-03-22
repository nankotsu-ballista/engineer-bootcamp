from collections import deque
n=int(input())
A=list(map(int,input().split()))
A.sort()
ans=deque()
#print(A)
ruiseki=[0]*(10**6+1)
ruiseki[0]=n
kuriagari=[0]*(10**6+1)
for i in range(n):
    ruiseki[A[i]]-=1
#print(ruiseki[:10**6])
tmpruiseki=0
for i in range(10**6):
    tmpruiseki+=ruiseki[i]
    ruiseki[i]=tmpruiseki
#print(ruiseki[:10**6])    
#print(kuriagari[:10**6])

for i in range(10**6):
    tmp=kuriagari[i]+ruiseki[i]
    ans.append(tmp%10)
    kuriagari[i+1]+=(tmp//10)
#print(ans)
while ans:
    t=ans.pop()
    if t==0:
        continue
    else:
        ans.append(t)
        break
ans=list(ans)
ans.reverse()
trueans=[]
for i in ans:
    trueans.append(str(i))
print("".join(trueans))

    




    
    
