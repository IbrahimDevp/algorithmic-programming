import math
Sx,Sy,Gx,Gy = map(int, input().split())
y = 0
x = 0

x = ((Sx*Gy)+(Gx*Sy))/(Sy+Gy)
print(x)