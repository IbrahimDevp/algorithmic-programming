N = int(input())
T = str(input())
x,y,d = 0,0,0
for i in range(N):
    if T[i] == 'S':
        if d%4 == 0:
            x+=1
        elif d%4 == 1:
            y-=1
        elif d%4 == 2:
            x-=1
        else:
            y+=1
    else:
        d+=1
print(x,y)


