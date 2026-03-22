from collections import deque
S=input()
stack=[]
for i in S:
    stack.append(i)
    check=True
    while check==True:
        last_three = stack[-3:]
        if last_three== ['A', 'B', 'C']:
            check=True
            for i in range(3):
                stack.pop()
        else:check=False
print("".join(map(str, stack)))