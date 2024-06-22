count = 0
N = int(input())

for B in range(1, 500+1):
    for A in range(B, 500+1):
        if A*A - B*B == N:
            count += 1

print(count)