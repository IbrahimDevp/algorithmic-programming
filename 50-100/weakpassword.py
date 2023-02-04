password = list(map(int, str(input())))
count = 1
for i in range(len(password)-1):
    if (password[i]+1)%10 == password[i+1]%10:
        count+=1
    else:
        count =0
print("Weak" if len(set(password)) == 1 or count >=3 else "Strong")