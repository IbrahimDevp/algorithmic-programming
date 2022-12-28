import math

a,b,d = map(int,input().split())
d = math.radians(d)
print(a*math.cos(d)-b*math.sin(d),b*math.cos(d)+a*math.sin(d))
