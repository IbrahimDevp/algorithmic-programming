N = int(input())
a = [0] * (N+1)
for i in map(int, input().split()) :
    a[i]+=1
for i in range(1,N+1):
    if a[i] == 3:
        print(i)
