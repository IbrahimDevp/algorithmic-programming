N,M = map(int,input().split())

A=list(list(map(int,input().split()))[1:] for _ in range(N))
common_values = A[0].intersection(*A)
print(len(common_values))
