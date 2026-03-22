n=int(input())
q=[]
count=0
while n!=0:
    if n%2==1:
        q.append("A")
        n-=1
    else:
        q.append("B")
        n=n//2
#     print(n)
# print(q)
q.reverse()
s = ''.join(map(str, q))
print(s)
