n = int(input())
loop_deadline = [int(input()) for _ in range(n)]
loop_deadline.sort()

answer = 1

for i in range(n):
    answer = max(answer, loop_deadline[i] * (n-i))

print(answer)