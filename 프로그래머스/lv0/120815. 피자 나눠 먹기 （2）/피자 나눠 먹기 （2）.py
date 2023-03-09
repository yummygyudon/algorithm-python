def solution(n):
    basicPizza = 1
    pizzaCount = 6
    while True :
        # print(pizzaCount)
        if pizzaCount % n == 0:
            break
        pizzaCount += 6
        basicPizza += 1
    return basicPizza