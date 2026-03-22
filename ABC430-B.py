N,M=map(int,input().split())
grid=[list(map(str,input().strip())) for _ in range(N)]
s=set()
for i in range(N-M+1):
    for k in range(N-M+1):
        tmp=""
        for ii in range(M):
            for kk in range(M):
                if grid[i+ii][k+kk]=="#":
                    tmp=tmp+str(ii*M+kk)
        #print(tmp)
        s.add(tmp)
#print(s)
print(len(s))