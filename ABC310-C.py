#N,K=map(int, input().split())
#arr = [list(map(int, input().split())) for _ in range(N)]
N = int(input())
#arr.sort(key=lambda x: x[0])
#print(arr)
t = set()
for _ in range(N):
    S = input()
    t.add(min(S, S[::-1]))
print(len(t))


