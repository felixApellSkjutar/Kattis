#A = number articles to publish
#I = the impact factor the Owners require
#Return: (A*I)-A+1

inArr = input().split(" ")

a = int(inArr[0])

i = int(inArr[1])

res = (a*i)-a+1

print(res)