X,K = map(int, input().split())

for i in range(K+1):
    
    X = round(X + 0.5, -i)
print(int(X))