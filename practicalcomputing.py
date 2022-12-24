N = int(input())

A = list(list() for _ in range (N))

for i in range(N):
    for j in range(i+1):
        if j==0 or j==i:
            print(1, end =' ')
            A[i].append(1)
        else:
            print(A[i-1][j-1] + A[i-1][j], end = ' ')
            A[i].append(A[i-1][j-1] + A[i-1][j])
    print()
