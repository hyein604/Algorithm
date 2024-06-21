from collections import deque

Y, X = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(Y)]
maxi = 0

for y in range(Y):
    for x in range(X):
        if graph[y][x] == 'L':
            visited = [[0 for _ in range(X)] for _ in range(Y)]     # 방문 했는가?
            dist = [[0 for _ in range(X)] for _ in range(Y)]     # 거리

            # BFS
            q = deque()
            q.append([y,x])     # 시작점
            visited[y][x] = 1

            while q:
                ey, ex = q.popleft()

                # 사방향 탐색(2차원 DP)
                for dy,dx in [[0,1], [1,0], [-1,0], [0,-1]]:
                    ny = ey + dy
                    nx = ex + dx
                    if 0 <= ny < Y and 0 <= nx < X:
                        if graph[ny][nx] == 'L':                # 갈곳이 땅이라면
                            if visited[ny][nx] == 0:            # 갈곳에 방문한적 없다면
                                visited[ny][nx] = 1             # 갈곳에 방문처리
                                dist[ny][nx] = dist[ey][ex] + 1 # 갈곳의 거리는 지금 있는곳에서 + 1
                                maxi = max(maxi, dist[ny][nx])
                                q.append([ny,nx])
print(maxi)