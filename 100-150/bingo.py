
A = list(list(map(int,input().split())) for _ in range(3))
N = int(input())
b = list(int(input()) for _ in range(N))

for i in range(3):
    for j in range(3):
        if A[i][j] in b:
            A[i][j]=-1
for i in range(3):
    cnt = 0
    for j in range(3):
        if A[i][j] == -1:
            cnt+=1
    if cnt == 3:
        print('Yes')
        exit()
for i in range(3):
    cnt = 0
    for j in range(3):
        if A[j][i] == -1:
            cnt+=1
    if cnt == 3:
        print('Yes')
        exit()
if A[0][0]+A[1][1]+A[2][2] == -3:
    print('Yes')
    exit()
if A[2][0]+A[1][1]+A[0][2] == -3:
    print('Yes')
    exit()
print('No')

        
    