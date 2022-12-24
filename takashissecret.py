N,X = map(int, input().split())

A = list(map(int,input().split()))
ans = list(0 for _ in range(100000))
i = X
while True:
    ans[i-1] = True
    i = A[i-1]
    if ans[i-1] == 1:
        break
count = 0
for i in range(100000):
    if ans[i] == 1:
        count +=1
print(count)
