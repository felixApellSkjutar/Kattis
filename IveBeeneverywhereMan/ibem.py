

var_in = int(input())


for i in range(var_in):
    var_cities = int(input())
    my_set = set()
    for j in range(var_cities):
        my_set.add(input())
    print(len(my_set))