num = int(input())

list1 = [list(input()) for _ in range(num)]


notfound = False
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if (list1[i] == list1[j]): notfound = True
c1 = [list(a) for a in zip(*list1)]
w = ['H','D','C','S']
w2 = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']

if all(x not in w for x in c1[0]):
    notfound = True
if all(y not in w2 for y in c1[1]):
    notfound = True

for element in c1[0]:
    if element not in w:
        notfound = True
for element in c1[1]:
    if element not in w2:
        notfound = True
if notfound:
    print('No')
else:
    print('Yes')
