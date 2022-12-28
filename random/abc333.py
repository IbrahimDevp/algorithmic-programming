A,B = map(int, input().split())
ans = False
for i in range(1,4):
    if (i*A*B%2 != 0):
        print('Yes')
        exit()
print('No')
