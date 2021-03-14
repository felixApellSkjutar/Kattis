#list(map(int, listan))

inArr = []

for i in range(5):
    inList = input().split(" ")

    inArr.append(list(map(int, inList)))

max = [0, 0]

for i in range(5):
    tmpSum = sum(inArr[i])
    if tmpSum > max[1]:
        max[1] = tmpSum
        max[0] = i+1

print(f'{max[0]} {max[1]}')