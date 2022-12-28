
N = str(input())
word= ''
for i in range(len(N)):
    if N[i] == '.':
        break
    word +=N[i]
print(word)