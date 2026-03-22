s=list(input())
ans=0
leftidx=[]
for i in range(len(s)-1):
    if int(s[i])+1==int(s[i+1]):
        leftidx.append(i)
#print(leftidx)
for i in leftidx:
    lnum=int(s[i])
    rnum=int(s[i+1])
    l=i
    r=i+1
    while l>=0 and r<len(s):
        if int(s[l])+1==int(s[r]) and int(s[l])==lnum and int(s[r])==rnum:
            ans+=1
            l-=1
            r+=1
        else:
            break
print(ans)
    
        
    