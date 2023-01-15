S = str(input())
T = str(input())
f = [0 for _ in range(150)]
f2 = [0 for _ in range(150)]
if len(S) == len(T):
    for i in range(len(S)):
        f[ord(S[i])] +=1
        f2[ord(T[i])] +=1
    if f == f2:
        print('Yes')
    else:
        print('No')
else:
    print('No')
    