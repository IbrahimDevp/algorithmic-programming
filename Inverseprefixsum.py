n = int(input())
arr = list(map(int, input().split()))
arr2 = []

for i in range(n):
        if (i == 0): arr2.append(arr[i])
        else: arr2.append(arr[i]-sum(arr2))

print(*arr2)