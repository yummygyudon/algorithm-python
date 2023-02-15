from sys import stdin

bin = stdin.readline()
c = list(map(int, stdin.readline().split()))
c.sort(reverse=True)
result = 0

for i in range(len(c)):
    if i <= 1:
        result += c[i]
    else:
        result += c[0]+c[i]

print(result)