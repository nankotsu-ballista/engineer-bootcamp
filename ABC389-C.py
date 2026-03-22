from collections import deque
q=int(input())
hebi=deque()
nuketahebi=0
nuketahebinokazu=0
hebisum=deque()
hebisum.append(0)
hebiruisekiwa=0
for i in range(q):
    A=list(map(int,input().split()))
    if A[0]==1:
        hebiruisekiwa+=A[1]
        hebi.append(A[1])
        hebisum.append(hebiruisekiwa)
    elif A[0]==2:
        boron=hebi.popleft()
        nuketahebi-=boron
        nuketahebinokazu+=1
    elif A[0]==3:
        hebihead=hebisum[A[1]-1+nuketahebinokazu]
        print(hebihead+nuketahebi)
# print(hebi)
# print(hebisum)
# print(nuketahebi)