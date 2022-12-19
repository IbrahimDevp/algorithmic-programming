N,K,Q = map(int,input().split())
sqr = list()
A = list(map(int,input().split()))
L = list(map(int,input().split()))

for i in range(0,Q):
    n = A[L[i]-1]+1
    if n > N or A[L[i]-1]+1 in A:
        continue
    else:
        A[L[i]-1] += 1
print(*A)