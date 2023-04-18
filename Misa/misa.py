#import time
#stime = time.time()
r,s = map(int, input().split(' '))


seats = []

for i in range(r):
    seats.append(list(input()))


shakes = 0


mirkoMax = 0
for i in range(r):
    for j in range(s):
        mirko = 0
        if seats[i][j] == 'o':
            if j != s-1 and seats[i][j+1] == 'o':
                shakes += 1
            if i != r-1 and j != (s-1) and seats[i+1][j+1] == 'o':
                shakes += 1
            if i != r-1 and seats[i+1][j] == 'o':
                shakes += 1
            if i != r-1 and j > 0 and seats[i+1][j-1] == 'o':
                shakes += 1
        else:
            if j != s-1 and seats[i][j+1] == 'o':
                mirko += 1
            if i != r-1 and j != (s-1) and seats[i+1][j+1] == 'o':
                mirko += 1
            if i != r-1 and seats[i+1][j] == 'o':
                mirko += 1
            if i != r-1 and j > 0 and seats[i+1][j-1] == 'o':
                mirko += 1
            if j > 0 and seats[i][j-1] == 'o':
                mirko += 1
            if i > 0 and j > 0 and seats[i-1][j-1] == 'o':
                mirko += 1
            if i > 0 and seats[i-1][j] == 'o':
                mirko += 1
            if i > 0 and j != s-1 and seats[i-1][j+1] == 'o':
                mirko += 1
            if mirko > mirkoMax:
                mirkoMax = mirko

print(shakes+mirkoMax)
#atime = time.time()
#print(atime-stime)