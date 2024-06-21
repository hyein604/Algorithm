import sys
N = int(sys.stdin.readline())


def check_sosu(num):
    error = True
    if num == 1 or num == 0:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                error = False
                break
    return error


for i in range(N):
    a = int(sys.stdin.readline())
    for j in range(a, 5000000000):
        if check_sosu(j):
            print(j)
            break