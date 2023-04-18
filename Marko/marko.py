dictSize = int(input())

two = {'a','b','c'}
three = {'d','e','f'}
four = {'g','h','i'}
five = {'j','k','l'}
six = {'m','n','o'}
seven = {'p','q','r','s'}
eight = {'t','u','v'}
nine = {'w','x','y','z'}

arr = []

for i in range(0, dictSize):
    arr.append(input())

marko = input()

count = 0

for a in arr:
    str = ""
    for s in a:
        if s in two:
            str += '2'
        elif s in three:
            str += '3'
        elif s in four:
            str+='4'
        elif s in five:
            str+='5'
        elif s in six:
            str+='6'
        elif s in seven:
            str+='7'
        elif s in eight:
            str+='8'
        elif s in nine:
            str+='9'
    if str == marko:
        count += 1


print(count)