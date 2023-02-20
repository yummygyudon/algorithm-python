N = int(input())
SUGGEST = []
for _ in range(N) :
    SUGGEST.append(list(map(int, input().split())))

SUGGEST.sort(key = lambda x : (x[1],-x[0]))
from collections import deque
SUGGEST = deque(SUGGEST)
ACCEPT = []
for _ in range(N) :
    benefit, dueDate = SUGGEST.popleft()
    ACCEPT.append(benefit)
    ACCEPT.sort()
    if dueDate < len(ACCEPT) :
        ACCEPT.pop(0)

print(sum(ACCEPT))