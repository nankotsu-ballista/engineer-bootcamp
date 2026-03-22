from atcoder.segtree import SegTree
n,m=map(int,input().split())
A=list(map(int,input().split()))
tmpmod=0
ruisekimod=[0]
for i in range(n):
  tmpmod=(A[i]+tmpmod)%m
  ruisekimod.append(tmpmod)
#print(ruisekimod)
def op(a,b):
  return a+b
st = SegTree(op, 0, m)
modst = SegTree(op, 0, ruisekimod)
ans=0
for i in range(n):
  Sr=ruisekimod[i+1]
  SrSl=modst.prod(0,i+1)
  st.set(ruisekimod[i],st.get(ruisekimod[i])+1)
  msum=st.prod(ruisekimod[i+1]+1,m)
  ans+=(i+1)*Sr-SrSl+msum*m
  #print(Sr,SrSl,msum)
print(ans)
  
segt=[]
# for i in range(m):
#   segt.append(st.prod(i,i+1))
# print(segt)
# segt=[]
# for i in range(n):
#   segt.append(modst.prod(i,i+1))
# print(segt)