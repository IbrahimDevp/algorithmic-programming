s = str(input())
T = 'oxx'
for i in range(pow(10,5)):
    T += 'oxx'
if s not in T:
    print('No')
else:
    print('Yes')