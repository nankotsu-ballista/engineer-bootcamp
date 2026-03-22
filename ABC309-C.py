N,K=map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])
#print(arr)
sum=0
for i in range(N):
    sum += arr[i][1]
for i in range(N):
    if sum <= K:
        if i == 0:
            print(1)
            exit()
        else:
            print(arr[i-1][0]+1)
            exit()
    else:
        sum -=arr[i][1]
print(arr[N-1][0]+1)
    

