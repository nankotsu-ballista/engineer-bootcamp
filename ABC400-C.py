import math
N=int(input())
sum=0
for i in range(1,61):
    if 2**i > N:
        print(sum)
        exit()
    b = math.isqrt(N // (2**i))  # ← ここを修正！
    sum += (b-(b//2))
    #print(str(i)+":"+str(b))