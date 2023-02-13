N,L = map(int,input().split())
flvs = list()
for i in range(1,N+1):
    flvs.append(L+i-1)
ans = list()
ans2 = list()
for i in range(N):
     ans.append(sum(flvs) - flvs[i])
for i in range(N):
     ans2.append(abs(sum(flvs) - flvs[i]))
if sum(flvs) in ans or sum(flvs) in ans2:
     print(sum(flvs))
elif sum(flvs)< 0:
     print(min(ans))
else:
     print(max(ans))
    