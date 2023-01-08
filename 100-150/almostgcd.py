N = int(input())
A = list(map(int, input().split()))
A1 = list()
for _ in range (100000):
    A1.append(0)
for i in A:
    for j in reversed(range(2,i+1)):
        if i%j == 0:
            A1[j] += 1
ind = max(A1)
print(A1.index(ind))