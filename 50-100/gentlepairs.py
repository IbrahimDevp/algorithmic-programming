N = int(input())
count = 0
A = list(list(map(int,input().split())) for _ in range(N))

for i in range(N-1):
    for j in range(i+1,N):
        if A[j][0]-A[i][0] == 0:
            cal = 100
        else:
            cal = (A[j][1]-A[i][1])/(A[j][0]-A[i][0])
            if cal >= -1 and cal <= 1:
                count+=1

print(count)