import bisect
import math
import sys
import copy
#import numpy as np # Pypyでは使えない
from collections import deque,defaultdict,Counter
from itertools import permutations,combinations,product,accumulate
from array import array # 連続メモリ上の配列（数値型で使用，高速）
# al=[chr(ord('a') + i) for i in range(26)]
# Al=[chr(ord('A') + i) for i in range(26)]
DEBUG = False  # デバッグ時は True、本番環境では False
def debug_print(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
n=int(input())
A=list(map(int,input().split()))
for i in range(1,n-1):
    if A[i-1]==A[i] and A[i+1]==A[i]:
        print("Yes")
        exit()
print("No")