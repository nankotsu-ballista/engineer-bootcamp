import bisect
q=int(input())
total=0
trees=[]
beforecutpoint=0
nowcutpoint=0
for i in range(q):
    a=list(map(int,input().split()))
    if a[0]==1:
        trees.append(total)
    elif a[0]==2:
        total+=a[1]
    elif a[0]==3:
        #beforecutpoint=min(beforecutpoint,len(trees))
        #print(beforecutpoint)
        nowcutpoint=bisect.bisect_right(trees, total-a[1])
        ans=nowcutpoint-beforecutpoint
        beforecutpoint=nowcutpoint
        # print("doko"+str(total-a[1]))
        # print("bf:"+str(beforecutpoint))
        # print("nc:"+str(nowcutpoint))
        # print("tr:"+str(trees))
        # print("total:"+str(total))
        print(ans)

        
#print(trees)