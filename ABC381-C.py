n=int(input())
s=input()
global ans
ans=0
def nobiru(idx):
    global ans
    i=1
    #print("iku")
    while idx+i<n and idx-i>=0 and s[idx+i]=="2" and s[idx-i]=="1" :
        i+=1
    ans=max(ans,i)
for i in range(n):
    if s[i]=="/":
        nobiru(i)
print((ans-1)*2+1)