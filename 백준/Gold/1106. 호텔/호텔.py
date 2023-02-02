import sys
input = sys.stdin.readline

C, N = map(int,input().split())

TABLE = [[0,0] for _ in range(N)]
for i in range(N) :
    cost, customer = map(int, input().split())
    TABLE[i][0] = cost
    TABLE[i][1] = customer
TABLE.sort(key= lambda x : x[1], reverse=True)

OVERABLE = TABLE[0][1] 
CUSTOMER_PER_COST = [1e9] * (C + OVERABLE)
CUSTOMER_PER_COST[0] = 0

for cost, customer in TABLE:
    for i in range(customer, C+OVERABLE):
        CUSTOMER_PER_COST[i] = min(CUSTOMER_PER_COST[i], cost + CUSTOMER_PER_COST[i-customer])

print(min(CUSTOMER_PER_COST[C:]))