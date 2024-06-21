arr = list(str(input()).upper())
check = list('QWERTYUIOPASDFGHJKLZXCVBNM')
tmp = []
count = []
letter = []

for i in check:
    if i in arr:
        tmp.append([arr.count(i),i])
tmp = sorted(tmp)

for i in range(len(tmp)):
    count.append(tmp[i][0])
    letter.append(tmp[i][1])

if len(count) == 1:
    print(letter[0])
else:
    if count[-1] != count[-2]:
        print(letter[-1])
    else:
        print('?')