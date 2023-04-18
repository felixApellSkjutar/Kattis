inArr = []

for i in range(10):
    inArr.append(int(input()))

res = set()

for i in inArr:
    res.add(i%42)

print(len(res))