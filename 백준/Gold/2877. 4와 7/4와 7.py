import sys
input = sys.stdin.readline
K = int(input())

DEFAULT = ['4','7']

BIN = bin(K+1)
INDEXES = list(BIN[3:])
answer = ''
for idx in INDEXES :
    answer += DEFAULT[int(idx)]

print(answer)