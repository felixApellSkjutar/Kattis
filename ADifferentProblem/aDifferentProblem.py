inArr = list()

while True:
    try:
        inArr.append(input().split(' '))
    except:
        break

for x,y in inArr:
    print(abs(int(x) - int(y)))
