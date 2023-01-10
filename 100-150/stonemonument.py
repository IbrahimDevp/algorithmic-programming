a,b = map(int,input().split())
diff = b- a
tot = 0
for i in range(1,diff):
  tot+=i
print(tot-a)