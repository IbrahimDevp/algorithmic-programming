N, W= map(int,input().split())
A = list(map(int,input().split()))
unique = list()
for i in range(N):
    if A[i]<=W:
        unique.append(A[i])
    for j in range(i+1,N):
        if A[i]+A[j] <=W:
            unique.append(A[i]+A[j])
        for k in range(j+1,N):
            if A[i]+A[j]+A[k] <=W:
                unique.append(A[i]+A[j]+A[k])
unique = list(set(unique))
print(len(unique))
