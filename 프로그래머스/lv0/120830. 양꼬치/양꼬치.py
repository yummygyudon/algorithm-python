def solution(n, k):
    serviceBeverage = n // 10
    buyBeverage = (k - serviceBeverage) * 2000
    buyLamb = 12000 * n
    
    return buyLamb + buyBeverage