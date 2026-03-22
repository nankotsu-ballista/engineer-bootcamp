A,B,C=input().split()
A=int(A)
B=int(B)
C=int(C)
if A**2==B**2:
  Ax=2
  Bx=2
else:
  if A**2>B**2:
    Ax=3
    Bx=2
  else:
    Ax=2
    Bx=3
Axx=Ax
Bxx=Bx
if A<0:
  Axx=-1*Ax
if B<0:
  Bxx=-1*Bx
if C % 2 == 1:
  Cx=3
else:
  Cx=2
if Axx**Cx == Bxx**Cx:
  print("=")
if Axx**Cx < Bxx**Cx:
  print("<")
if Axx**Cx > Bxx**Cx:
  print(">")
  
