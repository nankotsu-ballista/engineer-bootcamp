n=int(input())
cubid=[[[0] * n for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        cubid[i][j]=list(map(int,input().split()))
sum = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            sum[i + 1][j + 1][k + 1] = (sum[i][j+1][k+1]
                                        + sum[i+1][j][k+1]
                                        + sum[i+1][j+1][k]
                                        - sum[i][j][k+1]
                                        - sum[i][j+1][k]
                                        - sum[i+1][j][k]
                                        + sum[i][j][k]
                                        + cubid[i][j][k])
q = int(input())
for _ in range(q):
    lx, rx, ly, ry, lz, rz = map(int, input().split())
    lx -= 1
    ly -= 1
    lz -= 1
    result = (sum[rx][ry][rz]
                - sum[lx][ry][rz]
                - sum[rx][ly][rz]
                - sum[rx][ry][lz]
                + sum[lx][ly][rz]
                + sum[lx][ry][lz]
                + sum[rx][ly][lz]
                - sum[lx][ly][lz])
    print(result)