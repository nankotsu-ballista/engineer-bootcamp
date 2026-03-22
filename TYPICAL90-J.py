import bisect
n=int(input())
one=[0]
two=[0]
onesum=0
twosum=0
for i in range(n):
    c,p=map(int,input().split())
    if c==1:
        onesum+=p
    else:
        twosum+=p
    one.append(onesum)
    two.append(twosum)
# print(one)
# print(two)
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    print((one[r]-one[l-1]),(two[r]-two[l-1]))