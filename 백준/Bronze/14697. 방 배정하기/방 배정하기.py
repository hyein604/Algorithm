a, b, c, n = map(int, input().split())
tmp = 0

for i in range(300):
    for j in range(300):
        for k in range(300):
            if i*a + j*b + k*c == n:
                tmp = 1
                break

if tmp == 1:
    print(1)
elif tmp == 0:
    print(0)