S=input()
T=input()
n=len(S)
countS =0
countT =0
m=0
countSalpha =[0] * 26
countTalpha =[0] * 26
for c in S.upper():
    if c.isalpha():
      countSalpha[ord(c) - ord('A')] += 1
    else:
      countS += 1
for c in T.upper():
    if c.isalpha():
      countTalpha[ord(c) - ord('A')] += 1
    else:
      countT += 1    
diff=[0] * 26
#print(countSalpha)
#print(countTalpha)
for i in range(26):
  #print(i)
  if i==0 or i==2 or i==3 or i==4 or i==14 or i==17 or i==19:
    diff[i] += (countSalpha[i]-countTalpha[i])
  else:
    if abs(countSalpha[i]-countTalpha[i]) == 0:
      m=2
    else:
      print("No")
      exit()
#print(diff)
#print(countS)
#print(countT)
for i in range(26):
  if diff[i]<0:
    countS=countS+diff[i]
  else:
    countT=countT-diff[i]
if countS<0 or countT<0:
  print("No")
else:
  print("Yes")