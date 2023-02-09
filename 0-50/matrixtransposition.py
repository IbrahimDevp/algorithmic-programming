H,W = map(int,input().split())
A =list(list(map(int,input().split())) for _ in range(H))
for i in range(W):
    for j in range(H):
        print(A[j][i],end=" ")
    print()