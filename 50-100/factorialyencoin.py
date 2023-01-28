from math import factorial

P = int(input())

coins_used = 0

for i in range(10, 0, -1):
    coin_value = factorial(i)
    coins_used += P // coin_value
    P %= coin_value
    
print(coins_used)