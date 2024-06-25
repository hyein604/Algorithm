k = int(input())
answer = []

for _ in range(k):
    a = int(input())
    if a == 0:
        answer.pop()
    else:
        answer.append(a)

print(sum(answer))