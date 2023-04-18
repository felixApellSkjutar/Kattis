nmbrCases = int(input())

for i in range(nmbrCases) :
    inArr = input().split()
    intArr = list(map(int, inArr))

    students = intArr.pop(0)
    ave = sum(intArr)/ students
    
    count = 0
    for j in intArr :
        if j > ave : 
            count += 1
    res = 100 * (count / students)
    print(f'{"%.3f" % res}%')
    

