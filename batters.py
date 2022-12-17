N = int(input())
A = list(map(int,input().split()))
P = 0
sqrs = [0,0,0,0]

for i in range (N):
    sqrs[0] += 1
    for j in range(A[i]):
        if sqrs[3] == 1:
            P+=1
        sqrs[3] = sqrs[2]
        sqrs[2] = sqrs[1]
        sqrs[1] = sqrs[0]
        sqrs[0] = 0
print(P)



