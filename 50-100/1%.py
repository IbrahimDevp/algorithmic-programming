import math
X = float(input())
ans = 100
years = 0
while(math.floor(ans) != X):
    per = ans * 0.01
    ans += per
    years +=1
print(years)