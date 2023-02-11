N = int(input())
arr = list(map(int, input().split()))
print(N-(sum(arr)%N))