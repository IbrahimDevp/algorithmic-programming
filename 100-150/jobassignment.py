N = int(input())
A = list()
B = list()
total = list()
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
res = 10000000000
for i in range(N):
    for j in range(N):
        res = min(res, A[i] + B[j] if i==j else max(A[i],B[j]))

print(res)