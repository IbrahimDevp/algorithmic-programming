A,B,C,K = map(int, input().split())
if K <= A:
    print(K)
elif K <= A+B:
    print(A)
else:
    S = K - (A+B)
    print(A-S)