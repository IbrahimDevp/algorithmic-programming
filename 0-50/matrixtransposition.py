H,W = map(int,input().split())
A =list(list(map(int,input().split())) for _ in range(H))
for i in (zip(*A)):
    print(*i)