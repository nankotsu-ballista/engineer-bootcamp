n=int(input())
imos=[0]*(2*10**5+1)
district=[]
for i in range(n):
    x,y=map(int,input().split())
    imos[x]+=1
    imos[y]-=1
check=False
count=0
tmp=[]
for i in range(2*10**5+1):
    count+=imos[i]
    if count>=1 and check==False:
        check=True
        l=i
    if count==0 and check==True:
        check=False
        print(l,i)