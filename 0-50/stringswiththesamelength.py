N = int(input())
S = list(input())
NS = list()
for i in range(N):
    NS.append(S[i])
    NS.append(S[N+i+1])
print("".join(NS))