a,b,c,d = map(int,input().split())
ans = list()
for i in range(a,b+1):
    for j in range(c,d+1):
        ans.append(i*j)
print(max(ans))