N = int(input())

A = list(map(int, input().split()))
Q = int(input())
ans = list()
for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 2:
        ans.append(A[query[1]-1])
    else:
        A[query[1]-1]=query[2]
for i in range(len(ans)):
    print(ans[i])