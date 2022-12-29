N,M = map(int,input().split())
A = list(map(int,input().split()))

total = sum(A)
less = total*1/(4*M)
cnt = 0

for i in A:
    if i >= less:
        cnt += 1

if cnt < M:
    print ("No")
else:
    print("Yes")
