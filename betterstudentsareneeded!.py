N,X,Y,Z = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
admitted = []
for i in range(1,X+1):
    max = 0
    loc = 0
    for j in range (1,len(A)+1):
        if max <= A[j-1]:
            max = A[j-1]
            loc = j
    if loc not in admitted:
        admitted.append(loc)
for i in range(1,Y+1):
    max = 0
    loc = 0
    for j in range (1,len(B)+1):
        if max <= B[j-1]:
            max = B[j-1]
            loc = j
    if loc not in admitted: 
        admitted.append(loc)
for i in range(1,Z+1):
    max = 0
    loc = 0
    for j in range (1,N+1):
        if max <= A[j-1]+B[j-1]:
            max = A[j-1]+B[j-1]
            loc = j
    if loc not in admitted: 
        admitted.append(loc)
admitted.sort()
for i in admitted:
    print(i)