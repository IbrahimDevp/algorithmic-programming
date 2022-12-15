L = []
for _ in range(10):
    s = str(input())
    L.append(s)
A,B,C,D = 0,0,0,0
max = 0
for i in range (10):
    if '#' in L[i]:
        if A == 0 and B == 0:
            A += 1 +i
            B += 1 +i
        else:
            B+=1
for i in range(10):
    for j in range(10):
        if '#' in L[i][j]:
            if C == 0 and D == 0:
                C += 1 + j
                D += 1 + j
            else:
                if j+1 > D:
                    D = j+1
                if j+1 < C:
                    C = j + 1

print(A,B)
print(C,D)