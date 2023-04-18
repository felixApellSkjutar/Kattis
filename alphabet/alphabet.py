

arr = input()


ls = [1]*(len(arr))

for i in reversed(range(len(arr))):
    for j in range(i, len(arr)):
        if arr[i] < arr[j]:
            ls[i] = max(ls[i], ls[j]+1)


print(26-max(ls))
