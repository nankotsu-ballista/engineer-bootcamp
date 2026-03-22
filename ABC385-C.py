N=int(input())
H=list(map(int,input().split()))
ans=1  # -1 → 1 に変更（これだけ！）
for i in range(1,N):
    for j in range(N):
        count=0
        k=0
        first=H[j]
        while i*k+j<N:
            if first == H[i*k+j]:
                k+=1
                count += 1
            else:
                break
        ans=max(ans,count)
print(ans)