num = int(input())

list1 = [list(input()) for _ in range(num)]


notfound = False
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if (list1[i] == list1[j]): notfound = True
c1 = list(zip(*list1))
w = ['H','D','C','S']
w2 = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
if 'H' and 'D' and 'C' and 'S' not in c1[0]:
    notfound = True
if 'A' and '2' and '3' and '4' and '5' and '6' and '7' and '8' and '9' and 'T' and 'J' and 'Q' and 'K' not in c1[1]:
    notfound = True

if notfound:
    print('No')
else:
    print('Yes')
