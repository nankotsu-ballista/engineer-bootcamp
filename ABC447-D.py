from collections import deque
s=list(input())
acount=0#余裕のA
abcount=0
abccount=0
for i in s:
    if i=="A":
        acount+=1
    elif i=="B":
        if acount!=0:
            abcount+=1
            acount-=1
    elif i=="C":
        if abcount!=0:
            abccount+=1
            abcount-=1
print(abccount)