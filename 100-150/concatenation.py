import math
a,b= map(int,input().split())
a = str(a)+str(b)
ans = math.sqrt(int(a))
print('Yes' if ans*ans == int(a) and ans%1 == 0 else 'No')