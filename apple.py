X,Y,N = map(int,input().split())
result = 0
for i in range(0,N):
    for j in range(0,N):
        total = i*X + j*(Y*3)
        if((total%X + total%Y) == N):
            print(i,j)
            print(total)
            exit()
10%1