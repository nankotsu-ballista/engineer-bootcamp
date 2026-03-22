T=int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    A.sort(key=lambda x: -abs(x))
    if A.count(A[0]) == N:
        print("Yes")
        continue
    if A.count(A[0]) + A.count(-A[0]) == N and min(A.count(A[0]), A.count(-A[0])) == N // 2:
        print("Yes")
        continue


    #print(A)
    # 絶対値が等比的かチェック
    abscheck = True
    for i in range(1,N-1):
        if A[i] * A[i] != A[i-1] * A[i + 1]:
            abscheck = False
            break
    if abscheck == True:
        print("Yes")
    else:
        print("No")