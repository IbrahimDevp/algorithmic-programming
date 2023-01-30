N, M = map(int,input().split())
S = list(input() for _ in range(N))
T = list(list(set(input() for _ in range(M))))
count = 0
for i in range(len(T)):
    for j in range(N):
        if S[j][3:]==T[i]:
            count+=1
print(count)