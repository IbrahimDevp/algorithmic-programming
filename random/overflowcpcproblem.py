n = int(input())
lst = list(map(int, input().split()))

product = 1

if len(lst) < 99900:
    for num in lst:
        product *= num
    if product <= (2 ** 63 - 1):
        print(product)
    else:
        print(-1)
    exit()
else:
    for i in range(n):
        product *= lst[i]
        if product > (2**63 - 1):
            print(-1)
            exit()
print(product)