N,M=map(int,input().split())
A=list(map(int,input().split()))
idx=0
maxscore=0
scorelist=[0]*N
not_solve=[[] for _ in range(N)]
for i in range(N):
    S=input()
    score=0
    for j in range(M):
        if S[j]=="o":
            score+=A[j]
        elif S[j]=="x":
            not_solve[i].append(A[j])
    score+=i
    scorelist[i]=score
    if score>maxscore:
        maxscore=max(score,maxscore)
        idx=i
# print(idx)
# print(maxscore)
# print(scorelist)
# print(not_solve)
for i in range(N):
    if i == idx:
        print(0)
        continue
    S=not_solve[i]
    S.sort()
    S.reverse()
    diff=maxscore-scorelist[i]
    count=0
    for j in range(len(S)):
        
        diff-=S[j]
        count+=1
        if diff<= 0:
            break
    print(count)
        
        