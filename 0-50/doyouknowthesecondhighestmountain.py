N = int(input())
map = []
for i in range(N):
    a,b = input().split()
    map.append([int(b),a])
map.sort(reverse=True)
print(map[1][1])

