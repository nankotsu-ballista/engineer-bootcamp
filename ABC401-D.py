n,k=map(int,input().split())
s=list(input())
count=0
for i in range(len(s)):
    if s[i]=="o":
        if -1<i-1<n:
            s[i-1]="."
        if -1<i+1<n:
            s[i+1]="."
        count+=1
hatenacount=-1
tmp=0
if count==k:
    for i in range(len(s)):
        if s[i]=="?":
            s[i]="."
else:
    hatenacount=0
    for i in range(len(s)):
        if s[i]=="?":
            tmp+=1
        else:
            hatenacount+=(tmp//2+tmp%2)
            tmp=0
hatenacount+=(tmp//2+tmp%2)
#print(hatenacount)
#print(s)
tmp=0
if hatenacount==k-count:
    for i in range(len(s)):
        if s[i]=="?":
            tmp+=1
        else:
            #print(i)
            if tmp%2==1:
                #print(i-tmp, i)
                for k in range(tmp):
                    if k%2==0:
                        s[i-tmp+k]="o"
                    else:
                        s[i-tmp+k]="."
            #print(s)
            tmp=0
        #print(tmp)
i=i+1
if tmp%2==1:
    #print(i-tmp, i)
    for k in range(tmp):
        if k%2==0:
            s[i-tmp+k]="o"
        else:
            s[i-tmp+k]="."
result = ''.join(s)
print(result)
        