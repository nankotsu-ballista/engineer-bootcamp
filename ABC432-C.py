n,x,y=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
#print(A)
maximum=A[0]*y
ans=A[0]
for i in range(1,n):
    #print(i)
    if (A[i]*y-maximum)%(y-x)!=0:
        print(-1)
        exit()
    else:
        #print("hiku",(A[i]*y-maximum))
        if (maximum-((A[i]*y-maximum)//(y-x))*x)//y<0:
            print(-1)
            exit()
        ans+=(maximum-((A[i]*y-maximum)//(y-x))*x)//y
print(ans)