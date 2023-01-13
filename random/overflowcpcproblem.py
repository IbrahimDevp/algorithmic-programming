n = int(input())
lst = list(map(int, input().split()))

product = 1

for num in lst:
    product *= num
    if product > (2**63 - 1) and len(lst) > 99900:
        print(-1)
        exit()
if product <= (2 ** 63 - 1):
    print(product)
else:
    print(-1)
