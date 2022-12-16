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
# tA = A.copy()
# tB = B.copy()
# for i in range(Z):
#     max = 0
#     loc = 0
#     for j in range (N):
#         if max < tA[j]+tB[j]:
#             max = tA[j]+tB[j]
#             loc = j+1
#     tA[loc-1],tB[loc-1] = -1,-1
#     admitted.append(loc)
# tA = A.copy()
# tB = B.copy()
# for i in range(X):
#     max = 0
#     loc = 0
#     for j in range (1,len(tA)+1):
#         if max < tA[j-1]:
#             max = tA[j-1]
#             loc = j
#     tA[loc-1] = -1
#     admitted.append(loc)
# tA = A.copy()
# tB = B.copy()
# for i in range(Y):
#     max = 0
#     loc = 0
#     for j in range (1,len(tB)+1):
#         if max <= tB[j-1]:
#             max = tB[j-1]
#             loc = j
#     tB[loc-1] = -1
#     admitted.append(loc)
# admitted.sort()
# for i in admitted:
#     print(i)