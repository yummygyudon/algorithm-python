N = int(input())
score = [0]+[ int(input()) for _ in range(N)] + [0]
# 끝에 0을 하나 더 주어야 런타임 에러 안남
d = [0]*(N+2)
d[1] = score[1]
d[2] = d[1]+score[2]

for i in range(3,N+1) :
    d[i] = max(d[i-3]+score[i-1], d[i-2])+score[i]
    # d[i+1] = max(d[i-1] + score[i-1], d[i-2] + score[i-2])
print(score)
print(d)
print(d[N])
# print(d[N])
