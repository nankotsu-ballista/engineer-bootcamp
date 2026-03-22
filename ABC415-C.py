T=int(input())
for _ in range(T):
    n=int(input())
    s=input()
    safe=[0]*(1<<n)
    safe[0]=1
    for i in range(1<<n):
        if safe[i] == 0:
            continue
        for j in range(n):
            if (i >> j) & 1:
                continue
            next_state = i | (1 << j)  # j番目を追加した新状態
            #print(next_state)
            if s[next_state-1] == '0':   # その状態が合法なら
                safe[next_state] = 1     # その状態に遷移可能とマーク
        
    if safe[(1<<n)-1]:
        print("Yes")
    else:
        print("No")