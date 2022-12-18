N = int(input())
a = list(map(int,input().split()))
curr = a[0]
for i in range(1,len(a)):
    if curr < a[i]:
        curr = a[i]
    else:
        break
print(curr)