N,K = map(int,input().split())
word = list(input())
for i in range(N):
    if word[i] == 'o' and K>0:
        K-=1
    elif K == 0:
        word[i] = 'x'
print("".join(word))
