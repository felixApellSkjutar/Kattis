nmbrProblems = 0
inArr = input().split(";")

nmbrProblems += len(inArr)

filteredArr = list(filter(lambda x : "-" in x, inArr))

for i in filteredArr:
    f,s = list(map(int, i.split("-")))
    nmbrProblems += (s-f)

print(nmbrProblems)