N,A,B = map(int, input().split())

anslist=list()
for i in range(1,N+1):
        sumn = sum([int(j) for j in str(i)])
        if sumn >= A and sumn <= B:
            anslist.append(i)
print(sum(anslist))