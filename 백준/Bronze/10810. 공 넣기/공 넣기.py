n, m = map(int, input().split())
answer = [0 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i-1, j):
        answer[l] = k

print(* answer)