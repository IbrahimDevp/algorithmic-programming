T = int(input())

while T > 0:
    count = 0
    input()
    A = list(map(int,input().split()))
    for i in range(len(A)):
        if A[i]%2!=0:
            count+=1
    T-=1
    print(count)