H,M = map(int,input().split())

while True:
    A,C=H//10,H%10
    B,D=H//10,M%10
    AC = int(str(A)+str(B))
    BD = int(str(C)+str(D))
    if 0 <= AC <= 23 and 0 <= BD <= 59:
        break
    M+=1
    if M == 60:
        H+=1
        M=0
    if H == 24:
        H = 0
print(H,M)

