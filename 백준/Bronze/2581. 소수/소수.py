M = int(input())
N = int(input())
numbers = []

def check_sosu(N):
    if N == 0 or N == 1:
        return False
    for i in range(2,int(N**0.5)+1):
        if N % i == 0:
            return False
    return True

for i in range(M, N + 1):
    if check_sosu(i):
        numbers.append(i)

if len(numbers) == 0:
    print(-1)
else:
    print(sum(numbers))
    print(min(numbers))