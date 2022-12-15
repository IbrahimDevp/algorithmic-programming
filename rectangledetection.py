L = [list(input()) for _ in range (10)]
ans = []
for i in range(10):
    for j in range(10):
        if L[i][j] == '#':
            ans.append((i+1,j+1))

print(ans[0][0],ans[-1][0])
print(ans[0][1],ans[-1][1])
