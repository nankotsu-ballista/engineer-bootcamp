import sys 
sys.setrecursionlimit(10 ** 6)
n,m = map(int, input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
check=[-1]*(n+1)
nums=[[] for _ in range(n+1)]
for i in range(m):
    nums[a[i]].append(b[i])
    nums[b[i]].append(a[i])
def dfs(i):
    q=nums[i]
    for j in range(len(q)):
        if check[q[j]]==-1:
            if check[i]==1:
                check[q[j]]=0
                dfs(q[j])
            else:
                check[q[j]]=1
                dfs(q[j])
        else:
            if check[i]==check[q[j]]:
                print("No")
                # print(i)
                # print(q[j])
                # print(nums)
                # print(check)
                exit()
for i in range(1, n+1):
    if check[i] == -1:
        check[i] = 0          # ★成分の起点に色を付けてからDFS
        dfs(i)
# print(nums)
# print(check)
print("Yes")