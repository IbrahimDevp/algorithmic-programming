import math
def iswhole(n):
    return n%1 ==0
N,D = map(int, input().split())
count = 0
X = list(list(map(int,input().split())) for _ in range(N))
for i in range (N):
    for j in range (i+1,N):
        tot = 0
        for k in range(D):
            tot += pow(abs(X[i][k]-X[j][k]),2)
        if iswhole(math.sqrt(tot)):
            count+=1
print(count)
