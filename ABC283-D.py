from collections import defaultdict,deque
s=input()
s=list(s)
stack=[]
q=deque()
sujilist=defaultdict(int)
for i in range(len(s)):
    if s[i]=="(":
        stack.append(i)
    elif s[i]==")":
        left=stack.pop()
        while q:
            idx,suji=q.pop()
            if left>idx:
                q.append((idx,suji))
                break
            else:
                sujilist[suji]-=1
                
    else:
        if sujilist[s[i]]!=0:
            print("No")
            exit()
        q.append((i,s[i]))
        sujilist[s[i]]+=1
print("Yes")
        