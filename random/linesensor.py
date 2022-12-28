H,W = map(int,input().split())

list1 = [list(input()) for _ in range(H)]

list1 = list(zip(*list1))

for i in range(W):
    print(list1[i].count('#'), end = ' ')

