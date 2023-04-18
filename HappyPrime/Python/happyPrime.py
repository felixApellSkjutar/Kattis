numTests = int(input())

def breakDown(nums:str):
    if int(nums) < 7:
        return int(nums)
    primeSum = sum(map(lambda x: int(x)**2, list(nums)))
    return breakDown(str(primeSum))


def primeCheck(prime):
    if prime%2 ==0:
        return False
    for i in range(3, int(prime**0.5)+1, 2):
        if prime%i == 0:
            return False
    return True

for i in range(numTests):
    inp = input().split(' ')
    k = int(inp[0])
    prime = int(inp[1])
    if prime != 1 and primeCheck(prime) and breakDown(str(prime)) == 1:
        print(f'{k} {prime} YES')
    else:
        print(f'{k} {prime} NO')