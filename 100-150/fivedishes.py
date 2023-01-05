dishes = list(int(input()) for _ in range(5))

spent = 0
item = 10
rep = 4
for i in range(5):
    cal = dishes[i]%10
    if cal < item and cal > 0:
        item = cal
        rep = i
save = dishes[-1]
dishes[-1] = dishes[rep]
dishes[rep] = save
for i in range(5):
    spent += dishes[i]
    cal = spent%10
    if spent%10 != 0 and i < 4:
        add = 10 - cal
        spent += add
print(spent)