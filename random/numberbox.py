number = int(input())

list1 = [list(map(int, list(input()))) for _ in range(number)]

dx = [1, 0, -1, 0, -1, 1, 1,-1]
dy = [0, 1, 0, -1, 1, -1, 1,-1]
ans = 0

for i in range(number):
    for j in range(number):
        for k in range(8):
            cur = 0
            x,y = i,j
            for _ in range (number):
                cur *= 10
                cur += list1[x][y]
                x += dx[k]+number
                y += dy[k]+number
                x%=number
                y%=number
            ans = max(ans,cur)
print(ans)
