inArr = input().split(' ')

capacity = inArr[0]
stations = inArr[1]

measurements = []
passengers = 0
for i in range(0, stations):
    inp = input().split(' ')
    left = inp[0]
    entered = inp[1]
    stayed = inp[2]
    