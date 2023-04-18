initArr = input().split(' ')

h = int(initArr[0])
w = int(initArr[1])
n = int(initArr[2])

bricks = input().split(' ')
height = 0
layer = 0


for b in bricks:
    if height < h:
        layer += int(b)
        if layer == w:
            layer = 0
            height += 1
        elif layer > w:
            break 


if height == h:
    print("YES")
elif height < h:
    print("NO")
