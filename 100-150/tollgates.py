N,M,X = map(int, input().split())
cost1,cost2 = 0,0
A = list(map(int, input().split()))
for i in A:
    if i < X:
        cost1+=1
    if i > X:
        cost2+=1
else:
    print (min(cost1,cost2))