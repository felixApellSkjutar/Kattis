
test_cases = int(input())



for i in range(test_cases):
    x  = list(map(int, input().split())) #Ska ge lista av ints och splitta 
    var_indices = x[0]
    x.remove(var_indices)
    print(sum(x) - (var_indices-1))