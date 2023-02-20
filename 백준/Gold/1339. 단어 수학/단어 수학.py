import sys
input = sys.stdin.readline

N = int(input())
ALP_VAL_MAP = dict()

for _ in range(N) :
    word = list(input().rstrip())
    size = len(word)-1
    for i in range(len(word)) :
        if word[i] not in ALP_VAL_MAP.keys() :
            ALP_VAL_MAP[word[i]] = 1 * (10 ** (size - i))
        else :
            ALP_VAL_MAP[word[i]] = ALP_VAL_MAP.get(word[i]) + 1 * (10 ** (size - i))

ALP_VAL_MAP = list(ALP_VAL_MAP.items())
ALP_VAL_MAP.sort(key=lambda x : x[1], reverse=True)

result = 0
MAX = 9
for alp, value in ALP_VAL_MAP :
    result += (MAX * value)
    MAX -= 1
print(result)