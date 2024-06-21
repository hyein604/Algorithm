N = int(input())
score = list(map(int,input().split()))
answer = []

for i in range(N):
    answer.append(score[i] / max(score) * 100)

print(sum(answer)/N)