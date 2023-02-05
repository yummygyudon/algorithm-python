CRYPTO_NUM = list(input().rstrip())
if CRYPTO_NUM[0] == '0' :
    print(0)
else :
    SIZE = len(CRYPTO_NUM)
    CRYPTO_NUM = ['0']+CRYPTO_NUM
    DP = [0] * (SIZE + 1)
    DP[0], DP[1] = 1, 1
    for i in range(2, SIZE+1) :
        if int(CRYPTO_NUM[i]) > 0 :
            DP[i] += DP[i-1]
        if CRYPTO_NUM[i-1] == '0' :
            continue
        if (CRYPTO_NUM[i-1] == '1') or (CRYPTO_NUM[i-1] == '2' and int(CRYPTO_NUM[i]) <= 6) :
            DP[i] += DP[i-2]
    print(DP[SIZE]%1_000_000)