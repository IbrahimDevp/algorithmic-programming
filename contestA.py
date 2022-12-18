for _ in range(int(input())):
    n = int(input())
    arr = input()
    res = int(arr[0])
    for i in range(1,n):
        if res == 1 and arr[i] == '1':
            print('-',end = '')
            res = 0
        else:
            print('+', end='')
            res += int(arr[i])
    print()