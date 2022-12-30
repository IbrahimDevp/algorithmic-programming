A,B = map(int, input().split())

min = True
num = 0
sockets = 0
if B == 1:
    print(0)
    exit()
while (min):
    num += 1
    if sockets ==0:
        sockets+=A
    else:
        sockets+=A - 1
    if sockets >= B:
        min = False
print(num)