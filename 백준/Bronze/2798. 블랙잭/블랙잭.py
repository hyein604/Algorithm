N,M = map(int, input().split())
number = list(map(int, input().split()))
answer = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if number[i] + number[j] + number[k] <= M:
                answer = max(answer,number[i] + number[j] + number[k])

print(answer)