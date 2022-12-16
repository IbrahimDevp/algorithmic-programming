N,X,Y,Z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
admitted = []
tA = A.copy()
tB = B.copy()
tT = []
for i in range(N):
    tT.append(A[i]+B[i])
for i in range(X):
    mx = max(tA)
    indmax = tA.index(mx)
    if indmax+1 not in admitted:
        admitted.append(indmax+1)
    tA[indmax] = -1
    tB[indmax] = -1
    tT[indmax] = -1
for i in range(Y):
    mx = max(tB)
    indmax = tB.index(mx)
    if indmax+1 not in admitted:
        admitted.append(indmax+1)
    tB[indmax] = -1
    tT[indmax] = -1
for i in range(Z):
    mx = max(tT)
    indmax = tT.index(mx)
    if indmax+1 not in admitted:
        admitted.append(indmax+1)
    tT[indmax] = -1
admitted.sort()
for i in admitted:
    print (i)