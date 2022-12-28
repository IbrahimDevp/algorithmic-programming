A,B,C,D = map(int,input().split())
red = 0
operation = 0
if B >= C * D:
    print(-1)
    exit()
else:
    while A > D*red:
        A += B
        red +=C
        operation +=1
print(operation)
