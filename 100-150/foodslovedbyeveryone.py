N,M = map(int,input().split())

A=list(list(map(int,input().split()))[1:] for _ in range(N))
freq = list(0 for _ in range(31))
for i in range(N):
    for j in range(N):
        if i+1 in A[j]:
            freq[i+1] += 1
print(freq.count(N))