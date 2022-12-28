N,M = map(int,input().split())

cit = [[] for _ in range(N)]
for i in range(M):
    num1,num2 = map(int,input().split())
    cit[num1-1].append(num2)
    cit[num2-1].append(num1)

for i in range(N):
    print(str(len(cit[i])),*sorted(cit[i]))