import bisect
n=int(input())
A=list(map(int,input().split()))
B=[0]*(n)
for i in range(n):
    B[i]=A[i]
A.sort()
ruisekiwa=[]
sun=0
for i in range(n):
    sun+=A[i]
    ruisekiwa.append(sun)
# print(A)
# print(ruisekiwa)
# print(bisect.bisect_right(A,4))
S=[]
for i in range(n):
    idx=(bisect.bisect_right(A,B[i]))-1
    #print(ruisekiwa[-1]-ruisekiwa[idx])
    S.append(ruisekiwa[-1]-ruisekiwa[idx])
print(" ".join(map(str, S)))