n=int(input())
S=list(map(str,input().split()))
#print(S)
size=1
tries=[[[-1,0] for _ in range(26)]]

for i in S:
    s=list(i)
    nxt=0
    for k in range(len(s)):
        newnxt,times=tries[nxt][(ord(s[k])-97)][0],tries[nxt][(ord(s[k])-97)][1]
        tries[nxt][(ord(s[k])-97)][1]+=1
        if newnxt==-1:
            tries[nxt][(ord(s[k])-97)][0]=size
            size+=1
            tries.append([[-1,0] for _ in range(26)])
        nxt=newnxt
# for i in tries:
#     print(i)
ans=0
for i in S:
    s=list(i)
    nxt=0
    for k in range(len(s)):
        newnxt,times=tries[nxt][(ord(s[k])-97)][0],tries[nxt][(ord(s[k])-97)][1]
        ans+=times-1
        nxt=newnxt
print(ans//2)
        