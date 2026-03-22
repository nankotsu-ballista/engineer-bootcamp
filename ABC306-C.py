N=int(input())
fakelist=[0]*N
reallist=[0]*N
nums = list(map(int, input().split()))
for i in range(3*N):
    #print(i)
    #print(fakelist)
    num=nums[i]
    if fakelist[num-1]== 1:
        print(num , end=" ")
        fakelist[num-1] += 1
    else:
        fakelist[num-1] += 1
#print(reallist)
#for i in range(N):
    #index = reallist.index(min(reallist))
    #print(index + 1, end=" ")
    #reallist[index]=50000

