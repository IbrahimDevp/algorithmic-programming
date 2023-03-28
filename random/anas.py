n,m = map(int,input().split())
word = list(input())
word2 = word.copy()
for i in range(m):
    for j in range(n-1):
        if word[j]=='B' and word[j+1] =='G':
            word2[j] = 'G'
            word2[j+1] = 'B'
    word = word2.copy()
print(*word2, sep='') 