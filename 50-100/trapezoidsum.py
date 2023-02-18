N = int(input())
sumarr = 0
for _ in range(N):
    a,b=map(int,input().split())
    sumarr += (a+b) * (b-a + 1)/2
print(int(sumarr))