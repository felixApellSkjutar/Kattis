
nr_dataPoints = input()

datapoints = list(map(int(), input()))

len_list = len([n for n in datapoints if n < 0])

print(len_list)