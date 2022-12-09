N,M = map(int,input().split())

arr = [[],[]]

for _ in range(M):
    num1,num2 = map(int,input().split())
    arr[0].append(num1)
    arr[1].append(num2)

cit = list(list() for _ in range(N))
for i in range(M):
    cit[arr[0][i]-1].append(arr[1][i])
    cit[arr[1][i]-1].append(arr[0][i])

for i in range(N):
    cit[i].sort()
    print(str(len(cit[i])),end = ' ')
    print(*cit[i])