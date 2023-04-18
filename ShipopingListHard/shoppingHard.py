n, m = map(int, input().split())


setList = []

for i in range(n):
    setList.append(set(input().split(' ')))


itemSet = set.intersection(*setList)

print(len(itemSet))

for item in sorted(itemSet):
    print(item)