import itertools
def shogo(S1,S2,M):
    count=0
    for i in range(M):
       if S1[i]==S2[i]:
        count += 1
    if count == M-1:
        return True
    else:
        return False
        
    
N,M= map(int, input().split())
lines = [input().strip() for _ in range(N)]
                
                
for perm in itertools.permutations(lines):
    countS=0
    for i in range(N-1):
        #print(perm[i])
        if shogo(perm[i],perm[i+1],M):
            countS += 1
    if countS == N-1:
        print("Yes")
        exit()
    #print(countS)
    #print("---") 

print("No")
#if shogo("abcd","abed",4):
    #print("talofa")
        
        