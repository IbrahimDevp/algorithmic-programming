N = int(input())

p = list(map(int,input().split()))
p2 = sorted(p)
if p == p2:
    print('YES')
    exit()
else:
    for i in range(N-1):
        for j in range(i+1,N):
            tmp = p[i]
            tmp2 = p[j]
            p[i] = tmp2
            p[j] = tmp
            if p == p2:
                print('YES')
                exit()
            else:
                p[i] = tmp
                p[j] = tmp2
print('NO')
                
