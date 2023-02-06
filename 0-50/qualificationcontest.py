N,K = map(int,input().split())
names =list()
for _ in range(K):
    names.append(input())
names.sort()
for i in range(K):
    print(names[i])