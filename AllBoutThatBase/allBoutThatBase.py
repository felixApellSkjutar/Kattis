cases = int(input())
inArr = []
for i in range(0,cases):
    inArr.append(input())

#print(inArr)

def equation(eq):
    arr = eq.split()

    a = arr[0]
    op = arr[1]
    b = arr[2]
    c = arr[4]

    # a op b = c


def solver(a,op,b,c):
    if op == '*':
        multi(a,b,c)
    elif op == '/':
        div(a,b,c)
    elif op == '+':
        plus(a,b,c)
    elif op == '-':
        minus(a,b,c)



def multi(a,b,c):
    return None

def div(a,b,c):
    return None

def plus(a,b,c):
    return None

def minus(a,b,c):
    return None