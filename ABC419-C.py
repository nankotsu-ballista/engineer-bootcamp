n=int(input())
pointsx=[]
pointsy=[]
for i in range(n):
    r,c=list(map(int,input().split()))
    pointsx.append(r)
    pointsy.append(c)
# print(pointsx)
# print(pointsy)
a=(max(max(pointsy)-min(pointsy),max(pointsx)-min(pointsx)))
if a%2 == 1:
    print(a//2+1)
else:
    print(a//2)