#N,L,R=list(map(int,input().split()))
S=input()
# if R-L==0:
#     if S[R-1] != "o":
#         print("No")
#         exit()
#     print("Yes")
#     exit()
# count=0
# for i in range(L-1,R):
#     if S[i-1] == "o":
#         count+=1
#print(count)
# if count == R-L+1:
#     print("Yes")
# else:
#     print("No")
N=len(S)
ans=list(S)
find =1
for i in range(N):
    if find==1 and S[i]==".":
        ans[i]="o"
        find=0
    if S[i]=="#":
        find=1
    
#print(ans)
print("".join(ans))