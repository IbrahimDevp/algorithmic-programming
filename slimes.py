A,B,K = map(int,input().split())
ans = A
times = 0
for _ in range (1000000000):
    if ans >=B:
        print(times)
        exit()
    ans *=K
    times +=1
