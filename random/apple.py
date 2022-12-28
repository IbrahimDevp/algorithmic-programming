X,Y,N = map(int,input().split())
answer = 100000
for i in range(N+1):
    for j in range(N+1):
        total = i + (j*3)
        if(total == N):
            if(i*X+j*Y < answer):
                answer = i*X+j*Y

print(answer)