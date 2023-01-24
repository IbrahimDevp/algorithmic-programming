N,K = map(int, input().split())
freq = set()
for _ in range(K):
    input()
    for i in list(map(int,input().split())):
        freq.add(i)
print(N-len(freq))