N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

maxx = max(A)
minn = min (B)
count = 0
if maxx <= minn:
    for _ in range(maxx,minn+1):
        count+=1
else:
    print(count)
    exit()
print(count)