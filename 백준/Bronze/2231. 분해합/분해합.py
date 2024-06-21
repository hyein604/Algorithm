N = int(input())
answer = 0
for i in range(N):
    arr = list(map(int, str(i)))
    if i + sum(arr) == N:
        answer = i
        break
print(answer)