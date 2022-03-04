house = int(input())

red, green, blue = [], [], []
for _ in range(house) :
    r,g,b = map(int, input().split())
    red.append(r)
    green.append(g)
    blue.append(b)

result = 1001
cnt = 0

def paint(r,g,b) :
    global result
    if cnt == house-1 :
        result = min(r+g+b, result)
        return

for i in range(house) :
    paint(red[i],green[0],blue[0])
    paint(red[0], green[i], blue[0])
    paint(red[0], green[0], blue[i])

paint(cnt, red,green,blue)
print(result)
