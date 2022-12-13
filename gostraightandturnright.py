N = int(input())

T = str(input())

x,y = 0,0
ydir = False
neg = False
for i in range(N):
    if T[i] == 'S' and ydir == False and neg == False:
        x+=1
    elif T[i] == 'S' and ydir == False and neg == True:
        x-=1
    elif T[i] == 'S' and ydir == True and neg == False:
        y+=1
    elif T[i] == 'S' and ydir == True and neg == True:
        y-=1
    elif T[i] == 'R' and ydir == False and neg == False:
        ydir = True
        neg = True
    elif T[i] == 'R' and ydir == True and neg == True:
        ydir = False
        neg = True
    elif T[i] == 'R' and ydir == False and neg == True:
        ydir = True
        neg = False
    elif T[i] == 'R' and ydir == True and neg == False:
        ydir = False
        neg = False
print(x,y)


