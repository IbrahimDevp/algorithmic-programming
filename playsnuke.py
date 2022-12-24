N = int(input())
A = list()
P = list()
X = list()
minu = []
for _ in range(N):
    x,y,z= map(int,input().split())
    A.append(x)
    P.append(y)
    X.append(z)

for i in range(N):
    num = X[i] - A[i]
    if (num>0):
        minu.append(P[i])
large = pow(10,9)+1
minu.append(large)
if len(minu) == 1:
    print(-1)
else:
    print(min(minu))