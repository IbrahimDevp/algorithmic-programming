N,W = map(int, input().split())

A = list(map(int,input().split()))
cnt = list()
cnt2 = list()
ilist = list()
jlist = list()

for i in range (N):
    if A[i] <= W:
        if A[i] not in cnt:
            cnt.append(A[i]) 
    for j in range(N):
        if A[i]+A[j] <= W and i != j:
            cnt2.append(A[i]+A[j])
            ilist.append(i)
            jlist.append(j)
            if A[i]+A[j] not in cnt:
                cnt.append(A[i]+A[j])

for i in range(N):
    for j in range(len(cnt2)):
        if A[i]+cnt2[j] <= W and i!=ilist[j] and i!=jlist[j] and i!=j:
            if A[i]+cnt2[j] not in cnt:
                cnt.append(A[i]+cnt2[j])
 
print(len(cnt))
