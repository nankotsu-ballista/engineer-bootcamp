from collections import deque
n=int(input())
A=list(map(int,input().split()))
q=deque()
sum=0
for i in range(n):
    if q:
        count,number=q.pop()
        if number==A[i]:
            count+=1
            if count==number:
                sum-=count
            else:
                q.append((count,number))
        else:
            q.append((count,number))
            q.append((1,A[i]))
                
    else:
        q.append((1,A[i]))
    sum+=1
    print(sum)
    #print(q)