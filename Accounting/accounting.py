_, q = map(int, input().split())

general = 0
specials = {}
for _ in range(q):
    cmd, *args = input().split()
    if cmd == 'SET':
        specials[int(args[0])] = int(args[1])
        #accounts[int(args[1])-1] = int(args[2])
        #setAccount(int(args[1]), int(args[2]))
    elif cmd == 'PRINT':
        n = int(args[0])
        print(specials[n] if n in specials else general)
        #print(specials[args[0]] if int(args[0]) in specials else general)
        #print(accounts[int(args[1])-1])
        #printAccount(int(args[1]))
    else:
        general = int(args[0])
        specials.clear()