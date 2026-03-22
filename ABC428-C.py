from collections import deque
que=deque()
kakko=deque()
q=int(input())
length=0
quelength=0
lcount=0
rcount=0
check=False
for i in range(q):
    query=list(map(str,input().split()))
    if query[0]=="1":
        length+=1
        if query[1]=="(":
            lcount+=1
            kakko.append("(")
        if query[1]==")":
            rcount+=1
            kakko.append(")")
        if rcount>lcount:
            que.append(length-1)
            quelength+=1
        
    elif query[0]=="2":
        length-=1
        kak=kakko.pop()
        if kak=="(":
            lcount-=1
        if kak==")":
            rcount-=1
        if quelength!=0:
            queidx=que.pop()
            if queidx==length:
                quelength-=1
            else:
                que.append(queidx)
    if lcount==rcount and quelength==0:
        print("Yes")
    else:
        print("No")
    #print(kakko)