
nums = sorted([int(x) for x in input().split()])



s = input()

ordered = []

for c in s:
    if c == 'A':
        ordered.append(str(nums[0]))
    elif c == 'B':
        ordered.append(str(nums[1]))
    elif c == 'C':
        ordered.append(str(nums[2]))
    
print(" ".join(ordered))