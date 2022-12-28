N,M = map(int, input().split())
s = list(input() for _ in range(N))
total = 0
for i in range(N):
    for j in range(i+1,N):
        count = 0
        for k in range(M):
            if s[i][k] == 'o' or s[j][k] == 'o':
                count +=1
            else:
                break
        if (count == M):
            total +=1
print(total)