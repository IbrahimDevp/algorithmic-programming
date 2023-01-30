N, M = map(int,input().split())

S = list(input() for _ in range(N))
T = list(input() for _ in range(M))
T = list(set(T))
count = 0
for i in range(len(T)):
    for j in range(N):
        word = S[j]
        if word[3:]==T[i]:
            count+=1
print(count)