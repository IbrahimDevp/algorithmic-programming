N = int(input())
W = list(map(int,input().split()))

res = 100000000
S1,S2 = 0,0
for i in range(N-1):
    S1 += W[i]
    S2 = 0
    for j in range(i+1,N):
        S2 += W[j]
    res = min(res,abs(S1-S2))
print(res)