import bisect
N=int(input())
numbers=[]
for i in range(1,1000000):
    a=i**3
    a=str(a)
    l=len(a)
    if a==a[::-1]: 
        numbers.append(int(a))
numbers.sort()
t=bisect.bisect_left(numbers, N+1)
#print(numbers)
#print(t)
print(numbers[t-1])