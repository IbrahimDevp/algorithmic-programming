N = int(input())
A = list(tuple(list(map(int,input().split())) [1:]) for _ in range(N))
 
print(len(set(A)))