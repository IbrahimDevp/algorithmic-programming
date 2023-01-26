H,W,X,Y = map(int,input().split())

S = list(list(input()) for _ in range(H))
X-=1
Y-=1
count=0
for i in range (X,H-1):
    if S[i][Y] == '.':
        count+=1
    else:
        break
for i in range (Y,W-1):
    if S[X][i] == '.':
        count+=1
    else:
        break
for i in range (X,0,-1):
    if S[i][Y] == '.':
        count+=1
    else:
        break
for i in range (Y,0,-1):
    if S[X][i] == '.':
        count+=1
    else:
        break

print(count-2)