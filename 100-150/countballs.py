N,A,B=map(int,input().split())

count = A//(A+B)
A_count = count * A
rem = N%(A+B)

ans = A_count + min(rem,A)
print(ans)