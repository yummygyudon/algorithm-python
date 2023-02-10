import sys
input = sys.stdin.readline

K = int(input())
N = int(input())

# UNABLE = "x"*(K-1)

START_SEQ = [chr(i) for i in range(65, 65 + K)]
END_SEQ = list(input().rstrip())
LADDER = []
RANDOM_LAYER = 0
for i in range(N) :
    layer = list(input().rstrip())
    if layer[0] == '?' :
        RANDOM_LAYER = i
    LADDER.append(layer)


# print(START_SEQ)
# print(LADDER)
# print(RANDOM_LAYER)
# print(BEFORE_RANDOM)

"""
"-" 문자열 idx가 더 작으면 : 왼쪽으로 이동
"-" 문자열 idx가 더 크면 : 오른쪽으로 이동
"""

"""
RANDOM_LAYER 직전까지만
"""
for i in range(RANDOM_LAYER) :
    for k in range(K-1) :
        if LADDER[i][k] == "-" :
            START_SEQ[k], START_SEQ[k+1] = START_SEQ[k+1], START_SEQ[k]


"""
RANDOM_LAYER 직후까지만
"""
for i in range(N-1, RANDOM_LAYER, -1) :
    for k in range(K-1) :
        if LADDER[i][k] == "-" :
            END_SEQ[k], END_SEQ[k+1] = END_SEQ[k+1], END_SEQ[k]


RANDOM_LADDER = ["*"] * (K-1)

for i in range(K-1):
    if START_SEQ[i] == END_SEQ[i+1] and START_SEQ[i+1] == END_SEQ[i] :
        RANDOM_LADDER[i] = "-"
        START_SEQ[i], START_SEQ[i+1] = START_SEQ[i+1], START_SEQ[i]


"""
['C', 'A', 'D', 'B', 'E', 'G', 'F', 'H', 'I', 'J']
['C', 'A', 'B', 'D', 'G', 'E', 'F', 'H', 'J', 'I']

['C', 'A', 'B', 'D', 'G', 'E', 'F', 'H', 'J', 'I']
['C', 'A', 'B', 'D', 'G', 'E', 'F', 'H', 'J', 'I']
['*', '*', '-', '*', '-', '*', '*', '*', '-']
"""

if START_SEQ != END_SEQ :
    RANDOM_LADDER = ["x"]*(K-1)
print(''.join(RANDOM_LADDER))