N = int(input())
A = list()
B = list()
total = list()
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    total.append(a+b)
ind = total.index(min(total))
val = min(total)
ans = val
minn1 = 10000000
minn2 = 10000000
for i in range (N):
    if i != ind and B[i] < minn1:
        minn1 = B[i]
if minn1 < ans:
    ans = minn1
for i in range (N):
    if i != ind and A[i] < minn2:
        minn2 = A[i]
if minn2 < ans:
    ans = minn2

print(ans)




    
