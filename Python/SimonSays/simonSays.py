
cases = int(input())

testStr = 'Simon says'

for i in range(cases):
    line = input()
    
    if line[0:10] == testStr:
        print(line[10:])
