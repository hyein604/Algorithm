N, X = map(int,input().split())
arr = list(map(int,input().split()))
answer = []
for i in arr:
    if i < X:
        answer.append(i)
print(*answer)