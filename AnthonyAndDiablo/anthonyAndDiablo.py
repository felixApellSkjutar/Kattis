from cmath import sqrt
import math

inArr = input().split(' ')


a = float(inArr[0])
m = float(inArr[1])

r = math.sqrt(a/(math.pi))


if (2*r)*math.pi > m:
    print("Need more materials!")
else:
    print("Diablo is happy!")
