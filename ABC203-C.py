# coding: utf-8
# Your code here!

from collections import deque
N,K= map(int,input().split())
murabito=list()
for i in range(N):
    A,B=map(int,input().split())
    murabito.append([A,B])
murabito.sort(key=lambda x: x[0])
#print(murabito)
human=0
last=0
while K>0:
    #print(K)
    human=human+K
    K=0
    for j in range(last,N):
        if murabito[j][0]>human:
            break
        else:
            last=j+1
            K+=murabito[j][1]
print(human)
            
