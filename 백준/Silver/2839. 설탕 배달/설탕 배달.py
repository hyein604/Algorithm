n = int(input())
answer = 0

while n > 0:
    if n % 5 == 0:
        answer += n // 5
        n = 0
        break
    n -= 3
    answer += 1

if n == 0:
    print(answer)
else:
    print(-1)