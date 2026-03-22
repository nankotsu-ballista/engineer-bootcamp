N, L = map(int, input().split())
if L % 3 != 0:
    print(0)
    exit()
d = list(map(int, input().split()))
position = [0] * L
before=0
position[0]=1
for i in range(0,N-1):
  before=(before+d[i])%L
  position[before]=position[before]+1
sum=0
for i in range(0,L//3):
  sum=sum+(position[i]*position[i+L//3]*position[i+2*L//3])
print(sum)

