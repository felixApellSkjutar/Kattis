
x  = input().split()

lst = [0,0]

for i in range(len(x)):
    exp = 0
    for j in x[i]:
        lst[i] += int(j)*(10**exp)
        exp += 1


print(max(lst))
