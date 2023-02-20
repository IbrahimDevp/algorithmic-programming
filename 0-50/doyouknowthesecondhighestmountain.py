N = int(input())
map = {}
num = list()
for i in range(N):
    a,b = input().split()
    num.append(int(b))
    map[int(b)] = a
num.sort(reverse=True)
print(map[num[1]])

