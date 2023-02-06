N,K = map(int,input().split())
names = [input() for _ in range (K)]
print(*sorted(names), sep="\n")