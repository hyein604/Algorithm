n = int(input())
m = 0
for i in range(999999999):
    if m == n:
        print(i - 1)
        break
    if '666' in str(i):
        m += 1