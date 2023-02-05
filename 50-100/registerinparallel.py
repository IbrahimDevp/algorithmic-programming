N = int(input())

A = list(map(int,input().split()))
ans=0
for i in range(len(A)):
    ans += 1/A[i]
print(1/ans)