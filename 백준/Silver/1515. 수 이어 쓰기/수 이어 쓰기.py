from sys import stdin
input = stdin.readline
NUMBERS = list(input().rstrip())
start = 0
while True :
    start += 1
    number = list(str(start))
    while number and NUMBERS :
        if number[0] == NUMBERS[0] :
            NUMBERS.pop(0)
        number.pop(0)
    if len(NUMBERS) == 0 :
        print(start)
        break
