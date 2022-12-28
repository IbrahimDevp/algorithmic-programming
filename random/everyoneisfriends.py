N,M = map(int,input().split())

X = [list(map(int, input().split()[1:])) for _ in range(M)]

count =0
for i in range(1,N+1):
    for j in range(i+1, N+1):
        exist = False
        for x in X:
            if i in x and j in x:
                exist = True
                break
        if not(exist):
            print('No')
            exit()
print('Yes')