X,Y,Z=map(int,input().split())
S=input()
N=len(S)
inf = float('inf')
dp=[[inf]*2 for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
        target = 0 if S[i] == 'a' else 1
        for caps in range(2):  # caps: 現在の CapsLock 状態
            for next_caps in range(2):  # 次に移る CapsLock 状態
                cost = dp[i][caps]
                if caps != next_caps:
                    cost += Z  # 状態切り替えにZミリ秒かかる

                if target == next_caps:
                    cost += X  # aキー単体で出せる
                else:
                    cost += Y  # Shift+a で出す必要がある

                dp[i + 1][next_caps] = min(dp[i + 1][next_caps], cost)

print(min(dp[N][0], dp[N][1]))