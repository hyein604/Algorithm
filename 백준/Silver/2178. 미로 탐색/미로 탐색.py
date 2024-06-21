from collections import deque

n, m = map(int, input().split())
table = [list(input()) for _ in range(n)]
visit = [[False for _ in range(m)] for _ in range(n)]
dist = [[0 for _ in range(m)] for _ in range(n)]

q = deque()
q.append([0, 0])
dist[0][0] = 1
visit[0][0] = True

while q:
    if dist[n-1][m-1] != 0:
        break
    ey, ex = q.popleft()

    # 사방향 탐색
    for dy, dx in [[0,1], [1,0], [-1,0], [0,-1]]:
        ny = ey + dy
        nx = ex + dx
        if 0 <= ny < n and 0 <= nx < m:
            if table[ny][nx] == '1':
                if not visit[ny][nx]:
                    visit[ny][nx] = True
                    dist[ny][nx] = dist[ey][ex] + 1
                    q.append([ny, nx])

print(dist[n-1][m-1])