from collections import deque
n,s=map(int,input().split())
anoset=set()
anoset.add(0)
moji=[[[]for _ in range(10001)]for _ in range(501)]
for i in range(n):
    tmp=list(anoset)
    anoset=set()
    a,b=map(int,input().split())
    for num in tmp:
        if num+a<=10000 and num+a not in anoset:
            anoset.add(num+a)
            moji[i+1][num+a]=moji[i][num]+["H"]
        if num+b<=10000 and num+b not in anoset:
            anoset.add(num+b)
            moji[i+1][num+b]=moji[i][num]+["T"]
    # print(moji[i+1][:100])
    # print(anoset)
if len(moji[n][s])==n:
    print("Yes")
    print("".join(moji[n][s]))
else:
    print("No")

    