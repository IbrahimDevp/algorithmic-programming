N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))
cnt = 100000000000
for i in range(N):
    temp = T-H[i]*0.006
    if abs(temp-A) < cnt:
        ans = i + 1
        cnt =abs(temp-A)
print(ans)