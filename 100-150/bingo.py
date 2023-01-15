A = list(list(map(int,input().split())) for _ in range(3))
N = int(input())
b = list(int(input()) for _ in range(N))
f,s=0,0
for i in range(3):
    for j in range(3):
        if A[i][j] in b:
            A[i][j]=-1
            if i-j==0:
                f-=1
            if i+j==len(A)-1:
                s-=1

for i in range(3):
    column = [row[i] for row in A]
    if sum(A[i])==-3 or sum(column)==-3 or f == -3 or s == -3:
        print('Yes')
        exit()
print('No')
    