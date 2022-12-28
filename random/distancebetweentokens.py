H,W = map(int, input().split())
strings = list(str(input()) for _ in range(H))
loc = []
for i in range(H):
    for j in range(W):
        if strings[i][j] == 'o': loc.append([i,j])
print(abs(loc[0][0]-loc[1][0])+abs(loc[0][1]-loc[1][1]))
