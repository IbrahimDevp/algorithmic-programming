N = int(input())
S = list(input())
for i in S:
    i = ord(i)+ N%26
    print(chr(i-26) if i > 90 else chr(i),end='')