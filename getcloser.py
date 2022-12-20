import math

A,B = map(int, input().split())

d = math.sqrt(pow(A,2)+pow(B,2))
print(A/d,B/d)