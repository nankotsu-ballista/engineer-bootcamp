k,m=map(int,input().split())
mod=10007*m
ans=0
double=[0]*(101)
double[1]=1
for i in range(1,100):
    double[i+1]=(double[i]+double[i]*pow(10,2**(i-1), mod))%mod
#print(double)

kakoketa=0
items=[]
for i in range(k):
    c,l=map(int,input().split())
    items.append((c,l))
items.reverse()

for i in range(k):
    c,l=items[i]
    tm=(list(bin(l)[2:]))
    #print(tm)
    tmp=0
    tmpketa=0
    leng=len(tm)
    for kl in range(leng):
        if tm[kl]=="1":
            tmp=(tmp+c*double[leng-kl]*pow(10,tmpketa, mod))%mod
            tmpketa+=2**(leng-kl-1)
        #print(tmpketa,leng-kl)
    #print(tmp)    
    ans=ans+(tmp*pow(10,kakoketa, mod))%mod
    kakoketa+=l
print((ans%mod)//m)
