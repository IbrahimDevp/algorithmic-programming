a,b,c,d = map(int,input().split())
ans = list()
mx1 = max(a,b)
mx2 = max(c,d)
mn1 = min(a,b)
mn2 = min(c,d)


for _ in range (4):
    ans.append(mx1*mx2)
    ans.append(mx1*mn2)
    ans.append(mn1*mx2)
    ans.append(mn1*mn2)
print(max(ans))