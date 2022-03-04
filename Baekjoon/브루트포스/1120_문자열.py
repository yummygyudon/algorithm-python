import sys
word_A, word_B = sys.stdin.readline().rstrip().split()
word_A = list(word_A)
word_B = list(word_B)
Counts = []
for i in range(len(word_B)-len(word_A) +1) :
    Count = 0
    for k in range(len(word_A)):
        if word_A[k] != word_B[i+k] :
            Count +=1
    Counts.append(Count)
print(min(Counts))
# if len(word_A) == len(word_B) :
#     notEqual = 0
#     for i in range(len(word_A)) :
#         if word_A[i] != word_B[i] :
#             notEqual += 1
# print(notEqual)