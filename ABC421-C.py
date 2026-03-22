n=int(input())
s=input()
q=[]
odd=[]
even=[]
for i in range(n*2):
    if s[i]=="B":
        q.append(i)
#print(q)
for i in range(n):
    odd.append(i*2)
    even.append(i*2+1)
# print(odd)
# print(even)
odsum=0
evsum=0
for i in range(n):
    odsum+=abs(q[i]-odd[i])
    evsum+=abs(q[i]-even[i])
# print(evsum)
# print(odsum)
print(min(odsum,evsum))
    