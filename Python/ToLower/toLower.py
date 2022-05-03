tot = 0

inArr = input().split(' ')

problems = int(inArr[0])
testCases = int(inArr[1])
nmbrLines = problems * testCases

for i in range(0,problems):
    count = 0
    for j in range(0,testCases):
        
        if input()[1:].islower() :
            count = count +1
    if count == testCases:
        tot = tot +1

print(tot)