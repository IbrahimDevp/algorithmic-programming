import math
N = int(input())
A = list(map(int, input().split()))
tot,tot2 = 0 , 0
for i in range(len(A)):
    A[i] = abs(A[i])
    tot += A[i]
    tot2 += pow(A[i],2)

print(tot)
print(math.sqrt(tot2))
print (max(A))
