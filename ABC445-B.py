n=int(input())
items=[]
maxlen=-1
for i in range(n):
    s=input()
    items.append(s)
    maxlen=max(len(s),maxlen)
#print(maxlen)
for i in range(n):
    ss=items[i]
    ten="."*((maxlen-len(ss))//2)
    print(ten+ss+ten)
    
    