n = int(input())
arr = list(map(int, input().split()))

print(arr[0], end = ' ')
for i in range(1,n):
        print(arr[i]-arr[i-1],end = ' ')
