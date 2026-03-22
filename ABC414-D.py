n, m = map(int, input().split())
X=list(map(int, input().split()))
X.sort()
diff=[0]*(n-1)
#print(diff)
#print(X)
for i in range(n-1):
    diff[i]=X[i+1]-X[i]
n-1#本来の隙間
m-1#消せる隙間
#print(diff)
diff.sort()
sum=0
for i in range(n-m):
    sum += diff[i]
print(sum)
    
