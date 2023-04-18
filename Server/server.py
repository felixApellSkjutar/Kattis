parameters = input().split(' ')

nmbrTasks = int(parameters[0])
totTime = int(parameters[1])


c = 0
res = 0

tasks = input().split(' ')


for i in range(0,len(tasks)) : 
    
    c += int(tasks[i])
    if c > totTime:
        res = i
        break
    res += 1


print(res)