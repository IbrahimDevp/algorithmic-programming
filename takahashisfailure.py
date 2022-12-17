N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

mx = max(A)

for i in B:
    if A[i-1] == mx:
        print('Yes')
        exit()
print('No')