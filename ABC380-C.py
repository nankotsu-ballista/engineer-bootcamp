n,k=map(int,input().split())
s=input()
initial=[]
end=[]
check=False
for i in range(len(s)):
    if s[i]=="1" and check==False:
        initial.append(i)
        check=True
    if s[i]=="0" and check==True:
        end.append(i-1)
        check=False
if len(initial) == len(end)+1:
    end.append(i)
# print(initial)
# print(end)
s=list(s)
LL=initial[k-2]
LR=end[k-2]
RL=initial[k-1]
RR=end[k-1]
haba=RR-RL+1
# print(haba)
# print(LR)
for i in range(haba):
    s[LR+i+1]="1"
    s[RL+i]="0"
print("".join(str(x) for x in s))
