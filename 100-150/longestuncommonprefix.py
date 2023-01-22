N = int(input())
S = input()
for i in range(1,N):
    j = 0
    while i+j<N and S[j] != S[j+i]:
        j+=1
    print(j)
