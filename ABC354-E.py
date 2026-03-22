from collections import deque
n=int(input())
#print(2**18)
cards=[]
for i in range(n):
    a,b=map(int,input().split())
    cards.append((a,b))
combo=set()
q=deque()
for i in range(len(cards)-1):
    for k in range(i,len(cards)):
        if (cards[i][0]==cards[k][0] or cards[i][1]==cards[k][1]) and i!=k:
            combo.add((i,k))
#print(combo)
            
dp=[[0]*(1+2**(n)) for _ in range((n//2)+1)]
dp[0][0]=-1
for tp in range(n//2):
    for bit in range(2**n+1):
        if dp[tp][bit]!=0:
            for i,k in combo:
                if (bit&(1<<i)) or (bit&(1<<k)):
                    continue
                #print(bit,i,k,bit+2**i+2**k)
                if tp%2==0:
                    dp[tp][bit]=1
                else:
                    dp[tp][bit]=-1
                if tp%2==0:
                    dp[tp+1][bit+2**i+2**k]=1
                else:
                    dp[tp+1][bit+2**i+2**k]=-1
#print("olddp")
# for i in dp:
#     print(i)
                
for tp in range(n//2-1,-1,-1):
    for bit in range(2**n+1):
        check=False
        if dp[tp][bit]==0:
            continue
        if dp[tp][bit]!=0:
            for i,k in combo:
                if (bit&(1<<i)) or (bit&(1<<k)):
                    continue
                if tp%2==0:
                    if dp[tp+1][bit+2**i+2**k]==1:
                        check=True
                if tp%2==1:
                    if dp[tp+1][bit+2**i+2**k]==-1:
                        check=True
        if check==True:
            if tp%2==0:
                dp[tp][bit]=1
            if tp%2==1:
                dp[tp][bit]=-1
        if check==False:
            if tp%2==0:
                dp[tp][bit]=-1
            if tp%2==1:
                dp[tp][bit]=1
#         print(check,tp,bit)
# print("newdp")               
# for i in dp:
#     print(i)
if dp[0][0]==1:
    print("Takahashi")
else:
    print("Aoki")