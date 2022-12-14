N,K= map(int,input().split())
total = 0
for i in range(1,N+1):
    h =i*100
    for j in range(1,K+1):
        total += j + h
print(total)