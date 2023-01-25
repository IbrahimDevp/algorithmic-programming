A,B,C,K = map(int, input().split())
sum = 0
tempK = K
tempK-=A
if tempK <=0:
    print(K)
    exit()
tempK-=B
if tempK<=0:
    print(A)
    exit()
tempK-=C
if tempK>=0:
    print(A-C)
    exit()
C+=tempK
print(A-C)