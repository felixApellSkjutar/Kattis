frst = input()[::-1]

snd = input()[::-1]

diff = len(frst) - len(snd)

if diff > 0 :
    for i in range(0,diff) : 
        snd = snd + "0"
elif diff < 0 : 
    for i in range(0,-diff) : 
        frst = frst + "0"

frstArr = []
sndArr = []

for i in range(0,len(frst)) : 
    f = frst[i]
    s = snd[i]
    comp = int(f) - int(s)
    if comp > 0 :
        frstArr.insert(0,f)
    elif comp < 0 : 
        sndArr.insert(0,s)
    else : 
        frstArr.insert(0,f)
        sndArr.insert(0,s)

fut = ''.join(frstArr)
sut = ''.join(sndArr)

try:
    print(int(fut))
except :
    print("YODA")

try:
    print(int(sut))
except :
    print("YODA")
