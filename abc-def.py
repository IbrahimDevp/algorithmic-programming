a = list(input().split())
f,s=1,1

for i in range(3):
    f *= int(a[i])
    s *= int(a[i+3])
print((f-s)%998244353)