def dfs(n):
    global answer
    if n == N:  # N행까지 갔다면
        answer += 1
        return

    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] == 0:
            v1[j] = v2[n + j] = v3[n - j] = 1
            dfs(n+1)
            v1[j] = v2[n + j] = v3[n - j] = 0


N = int(input())
answer = 0
v1 = [0 for _ in range(N)]  # 열 방문
v2 = [0 for _ in range(2*N)]    # 오른쪽 하방 대각선 방문
v3 = [0 for _ in range(2*N)]    # 왼쪽쪽 하방 대각선 방문

dfs(0)
print(answer)