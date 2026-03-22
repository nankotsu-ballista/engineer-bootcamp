from collections import defaultdict

# 入力
n = int(input())
dice = []
sizes = []
for _ in range(n):
    line = list(map(int, input().split()))
    k = line[0]
    sizes.append(k)
    dice.append(line[1:])

# count[i][x] = サイコロiがxを何個持ってるか
count = []
for i in range(n):
    cnt = defaultdict(int)
    for x in dice[i]:
        cnt[x] += 1
    count.append(cnt)

# 各ペア(i, j)を全探索して、確率を計算
max_prob = 0.0
for i in range(n):
    for j in range(i + 1, n):
        prob = 0.0
        for x in count[i]:
            if x in count[j]:
                prob += (count[i][x] / sizes[i]) * (count[j][x] / sizes[j])
        max_prob = max(max_prob, prob)

# 出力（誤差対策）
print(f"{max_prob:.15f}")
