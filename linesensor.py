H,W = map(int,input().split())

list1 = [list(input()) for _ in range(H)]



ans = ''
for i in range(W):
    count = 0
    for j in range(H):
        if list1[j][i] == '#':
            count +=1
    ans += str(count) + ' '
print(ans)

