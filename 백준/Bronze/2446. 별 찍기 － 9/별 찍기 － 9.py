n = int(input())

for i in range(n):
    print(' '*i + '*'*(abs((n-i)*2-1)))

for i in range(n-2, -1, -1):
    print(' ' * i + '*' * (abs((n - i) * 2 - 1)))