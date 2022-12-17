N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
chance = list()
mxfixed = max(A)
for i in range (len(A)):
    mx = max(A)
    if mxfixed == mx:
        mxind = A.index(mx)
        chance.append(mxind+1)
        A[mxind] = -1
for i in chance:
    if i in B:
        print('Yes')
        exit()
print('No')