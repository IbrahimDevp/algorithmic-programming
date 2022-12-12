import math
X,K = map(int, input().split())

if pow(10,K)%X == 0:
    print(0)
elif (pow(10,K)%X >= pow(10,12)):
    Y = X%pow(10,K)
    print(abs(Y-X))
else:
    Y = X%pow(10,K)
    Y2 = abs(Y-pow(10,K))
    print(Y2+X)