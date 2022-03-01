import math
N = int(input())
n= 1
while True :
    v = n*(n+1)/2
    if v > N : # >= 는 불가능 등차수열 넘긴 뒤에 -1해서 마지막값
        print(n-1)
        break
    n += 1