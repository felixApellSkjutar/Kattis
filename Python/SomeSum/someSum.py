evenSet = {4,8}
oddSet = {2,6,10}
eitherSet = {1,3,5,7,9}

n = int(input())

if n in evenSet:
    print("Even")
elif n in oddSet:
    print("Odd")
elif n in eitherSet:
    print("Either")