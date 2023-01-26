H,W,X,Y = map(int,input().split())

S = list(list(input()) for _ in range(H))

ans=0
for i in range(X-1, H):
    if S[i][Y-1] == ".":
        ans += 1
    else:
        break
for i in range(X-1, -1, -1):
    if S[i][Y-1] == ".":
        ans += 1
    else:
        break
for i in range(Y-1, W):
    if S[X-1][i] == ".":
        ans += 1
    else:
        break
for i in range(Y-1, -1, -1):
    if S[X-1][i] == ".":
        ans += 1
    else:
        break
print(ans-3)