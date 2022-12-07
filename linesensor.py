H,W = map(int,input().split())

list1 = [[] for _ in range(W)]

for i in range(H):
    s = str(input())
    list1[i] = s

ans = ''
for i in range(W):
    count = 0
    for j in range(H):
        if list1[j][i] == '#':
            count +=1
    ans += str(count) + ' '
print(ans)

