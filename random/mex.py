N = int(input())
A = list(map(int,input().split()))
ans = 0
for i in range (N+1):
    if i not in A:
        ans = i
        break
print(ans)