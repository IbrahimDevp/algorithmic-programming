N = int(input())
word = list(input())
word2 = ""
for i in range(N-1):
    if word[i] == 'n' and word[i+1] =='a':
        word2 += word[i]
        word2 += 'y'
        if i+1 == N-1:
            word2+=word[-1]
    else:
        word2 += word[i]
        if i+1 == N-1:
            word2+=word[-1]
if len(word) == 1:
    print(*word)
else:
    print(word2)