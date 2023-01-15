S = str(input())
T = str(input())

for i in range(len(S)):
    word = S[-1]+S[:-1]
    S = word
    if (S == T):
        print('Yes')
        exit()
print('No')