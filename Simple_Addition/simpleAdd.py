lOne = input()[::-1]
lTwo = input()[::-1]


comp = len(lOne) - len(lTwo)

if comp > 0 : 
    for i in range(0,comp) : 
        lTwo = lTwo + "0"
elif comp < 0 : 
    for i in range(0,-comp):
        lOne = lOne + "0"
resArr = []
rest = 0

for i in range(0,len(lOne)): 
    f = int(lOne[i])
    s = int(lTwo[i])
    res = f + s + rest

    if res >= 10:
        rest = 1
        resArr.insert(0,str(res-10))
    else:
        rest = 0
        resArr.insert(0,str(res))
if rest == 1:
    resArr.insert(0,str(1))

resStr =''.join(resArr)
print(resStr)
