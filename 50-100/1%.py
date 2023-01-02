import math
X = int(input())
ans = 100
years = 0 
while ans < X:
    ans += ans//100
    years+=1
    print(ans)
print(years)