arrLen = int(input())

ls = list()

for i in range(arrLen):
    ls.append(int(input()))

resList = list(reversed(sorted(ls)))


sub = 0
tot= 0
for x in resList[2::3]:
    sub+=x

for i in resList:
    tot+=i


print(tot-sub)


