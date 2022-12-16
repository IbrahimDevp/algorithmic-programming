import math
N = int(input())
arr = list(map(int,input().split()))
p = 1
num = pow(2,63)-1
for i in arr:
    p*= i

if p<=num:
    print(p)
else:
    print(-1)
