L = []
for _ in range(10):
    s = str(input())
    L.append(s)
A,B,C,D = 0,0,0,0
for i in range (10):
    if '#' in L[i]:
        if A == 0 and B == 0:
            A += 1 +i
            B += 1 +i
        else:
            B+=1