N,L,R=list(map(int,input().split()))
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
for i in range(N):
    if S[i] != "o" and i <= R-1 and L-1 <= i:
        #print(i)
        print("No")
        exit()
print("Yes")