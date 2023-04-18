
inArr = int(input())

for i in range(inArr) :
    read = int(input())

    if read % 2 == 0:
        print(f'{read} is even')
    else:
        print(f'{read} is odd')