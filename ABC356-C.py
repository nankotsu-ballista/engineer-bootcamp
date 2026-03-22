N,M,K = map(int,(input().split()))

groups = []
Rs = []

for _ in range(M):
    line = input().split()
    C = int(line[0])
    A = list(map(int, line[1:C+1]))
    R = line[C+1]  # 数字でなく文字列ならint()しない
    groups.append((C, A))
    Rs.append(R)

ans=0
for bit in range(1 << N):
    count2=0
    for i in range(M):
        count=0
        for j in range(groups[i][0]):
            if (bit >> (groups[i][1][j])-1) & 1:
                count += 1
        if (count>=K and Rs[i]=="o") or (count<K and Rs[i]=="x"):
            count2+=1
    if count2 == M:
        ans +=1
print(ans)
