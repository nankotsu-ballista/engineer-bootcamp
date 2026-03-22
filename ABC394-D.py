S=input()
S=list(S)
q=[]
for i in range(len(S)):
    q.append(S[i])
    if len(q)>1:
        if (q[-1] == ")" and q[-2] == "(") or (q[-1] == ">" and q[-2] == "<") or (q[-1] == "]" and q[-2] == "["):
            q.pop()
            q.pop()

if len(q)==0:
    print("Yes")
else:
    print("No")
    
    
    
    
    