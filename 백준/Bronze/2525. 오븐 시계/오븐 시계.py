import sys
input = sys.stdin.readline
A, B = map(int,input().split())
C = int(input())
if B+C >= 60 :
  A += (B+C) // 60
  B += C % 60
  if A >= 24 :
    A -= 24
  if B >= 60 :
    B -= 60 
else :
  B += C

print(f"{A} {B}")