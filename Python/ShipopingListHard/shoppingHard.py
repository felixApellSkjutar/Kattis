a, b = [int(x) for x in input().split(' ')]

shoppingList = []
for i in range(0,a):
    shoppingList.append(input().split(' '))


shopDict = dict()

for x in shoppingList:
    for y in x:
        if (y in shopDict):
            shopDict[y] += 1

resArr = []

for s in shopDict:
    if shopDict[s] >= a:
        resArr.append(s)

print(len(resArr))
resArr.sort()
for s in resArr:
    print(s)
