

nmbrCases = int(input())


for i in range(nmbrCases):
    r,e,c = list(map(int, input().split(" ")))
    if r < (e-c):
        print("advertise")
    elif r == (e-c):
        print("does not matter")
    else:
        print("do not advertise")