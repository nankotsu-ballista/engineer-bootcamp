import bisect
h,w,n=map(int,input().split())
s=set()
dp=[[1]*w for _ in range(h)]
for i in range(n):
    a,b=map(int,input().split())
    s.add((a-1,b-1))
di=[0,1,1]
dk=[1,0,1]
for i in range(h-1,-1,-1):
    for k in range(w-1,-1,-1):
        tmp=[]
        if (i,k) in s:
            tmp.append(0)
        for d in range(3):
            ni=i+di[d]
            nk=k+dk[d]
            if ni<h and nk<w:
                tmp.append(dp[ni][nk]+1)
            else:
                tmp.append(1)
        #print(tmp)
        if tmp:
            dp[i][k]=min(tmp)

        #print(i,k)
# for i in dp:
#     print(i)
ans=0
for i in range(h):
    for k in range(w):
        ans+=dp[i][k]
print(ans)
        
                    
                
        
        

    