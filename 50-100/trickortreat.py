N,K = map(int, input().split())
freq = list(0 for _ in range(N))
for _ in range(K):
    input()
    A = list(map(int,input().split()))
    for i in range(len(A)):
        freq[A[i]-1]+=1
print(freq.count(0))