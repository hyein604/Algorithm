max = 1
level = 1
N = int(input())

for i in range(1,1000000000):
    if N <= max:
        print(level)
        break
    else:
        max += 6 * i
        level += 1