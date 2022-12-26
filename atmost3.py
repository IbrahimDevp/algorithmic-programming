N,W = map(int, input().split())

A = list(map(int,input().split()))
cnt = list()


for i in range (N):
    if A[i] <= W:
        if A[i] not in cnt:
            cnt.append(A[i]) 
    for j in range(N):
        if A[i]+A[j] <= W and i != j:
            if A[i]+A[j] not in cnt:
                cnt.append(A[i]+A[j])
        for k in range(N):
            if A[i]+A[j]+A[k] <= W and i!=j and i!=k and j!=k:
                if A[i]+A[j]+A[k] not in cnt:
                    cnt.append(A[i]+A[j]+A[k])

print(len(cnt))
