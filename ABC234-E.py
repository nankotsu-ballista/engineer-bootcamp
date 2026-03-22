setter=set()
num=int(input())
import bisect
for i in range(10):
    for k in range(10):
        s=[i]
        moji=str(i)
        sum=i
        while True:
            sum+=k
            if sum<10 and len(s)<17:
                s.append(sum)
                moji=moji+str(sum)
                setter.add(int(moji))
            else:
                break
for i in range(1,10):
    for k in range(9):
        s=[i]
        moji=str(i)
        sum=i
        while True:
            sum-=k
            if sum>-1 and len(s)<18:
                s.append(sum)
                moji=moji+str(sum)
                #print(moji)
                setter.add(int(moji))
            else:
                break
setter.discard(0)
setter=list(setter)
setter.sort()
idx=bisect.bisect_left(setter,num)
#print(setter)
if setter[idx]:
    print(setter[idx])
else:
    print(setter[idx])
    