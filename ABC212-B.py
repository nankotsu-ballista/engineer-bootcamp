s=list(map(int,(input().strip())))
t=[1,2,3,4,5,6,7,8,9,0]
if s[0]==s[1] and s[1]==s[2] and s[3]==s[2]:
    print("Weak")
    exit()
count=0
for i in range(3):
    if s[i+1]==t[s[i]]:
        count+=1

if count==3:
    print("Weak")
    exit()
print("Strong")