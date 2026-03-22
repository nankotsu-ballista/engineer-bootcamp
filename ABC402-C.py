N,M=map(int,input().split())


# for i in range(M):
#     A = input().split()
#     K=int(A[0])
#     for j in range(1,K+1):
#         meal[i].append(A[j])
# B = input().split()
recipes=[]

contains=[[] for _ in range(N+1)]

needed =[0] * M

for j in range(M):
    data = list(map(int,input().split()))
    k = data[0]
    ingredients = data[1:]
    recipes.append(ingredients)
    needed[j]=k
    for ing in ingredients:
        contains[ing].append(j)
# 回答の蓄積
ans = []
eaten = 0
B=list(map(int,input().split()))
# 各日、克服した食材B[i]に関連する料理だけ見て更新
for day in range(N):
    food = B[day]
    for r in contains[food]:
        needed[r] -= 1
        if needed[r] == 0:
            eaten += 1
    ans.append(eaten)
print(*ans, sep="\n")