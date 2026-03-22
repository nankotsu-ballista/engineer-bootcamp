N=int(input())
H=list(map(int,input().split()))
stack=[]
t=[]
for i in range(N-1,-1,-1):
    #print(stack)
    t.append(len(stack))
    while stack and stack[-1]<H[i]:
        stack.pop()
    stack.append(H[i])
t=t[::-1]
print(*t)

    