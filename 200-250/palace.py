N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))
D = list()
for i in H:
    D.append(T-i*0.006)
ans = 100000000000
D2=list()
for i in range(len(D)):
    ans = min(ans,abs(D[i]-A))
    D2.append(ans)
print(D2.index(ans)+1)