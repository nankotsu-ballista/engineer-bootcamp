n,x=map(int,input().split())
s=input()
s=list(s)
count=0
stack=[]
tmp=x
while tmp!=1:
    if(tmp%2)==1:
        stack.append("R")
    else:
        stack.append("L")
    tmp//=2
#print(stack)
stack.reverse()
tier=0
for i in range(n):
    if s[i]=="U":
        stack.pop()
    elif s[i]=="R":
        stack.append("R")
    elif s[i]=="L":
        stack.append("L")
#print(stack)
x=1
for i in range(len(stack)):
    if stack[i]=="U":
        x//=2
    elif stack[i]=="R":
        x*=2
        x+=1
    elif stack[i]=="L":
        x*=2
print(x)



#print(count)