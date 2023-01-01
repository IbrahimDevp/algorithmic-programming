N = int(input())
A = list()
B = list()
total = list()
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    total.append(a+b)
shortest = min(total)
ind = total.index(shortest)
shA=A[ind]
shB=B[ind]
A.pop(ind)
B.pop(ind)
minn = min(A)
minn2 = min(B)
if shA < shB:
    if minn2 <= shortest:
        print(minn2)
        exit()
    else:
        print(shortest)
        exit()
elif shA > shB:
    if minn <= shortest:
        print(minn)
        exit()
    else:
        print(shortest)
        exit()
else:
    if minn <= shortest:
        if minn2 <= minn:
            print(minn2)
            exit()
        else:
            print(minn)
            exit()
    if minn2 <= shortest:
        if minn <= minn2:
            print(minn)
            exit()
        else:
            print(minn2)
            exit()
print(shortest)

