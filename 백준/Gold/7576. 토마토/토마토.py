# from collections import deque
#
# m, n = map(int, input().split())    # 상자 가로 칸수, 상자 세로 칸수. 2이상 1000이하
# tomatoes = [list(map(int, input().split())) for _ in range(n)]  # 1은 익은 토마토, 0은 안익은 토마토, -1은 토마토 없음
# # visited = [[False for _ in range(m)] for _ in range(n)]
# minus = -1
#
#
# for i in range(n):  # y값. 세로
#     for j in range(m):  # x값. 가로
#         if tomatoes[i][j] == 1:
#             # and not visited[i][j]:
#
#             # BFS 시작
#             q = deque()
#             ey, ex = i, j
#             q.append([ey, ex])
#             # visited[ey][ex] = True
#
#             while q:
#                 ey, ex = q.popleft()
#
#                 # 사방향 탐색
#                 for dy, dx in [0, 1], [0, -1], [1, 0], [-1, 0]:     # 우, 좌, 하, 상
#                     ny = ey + dy
#                     nx = ex + dx
#
#                     if 0 <= ny < n and 0 <= nx < m:     # 방문할곳 좌표가 범위 내이고
#                         if tomatoes[ny][nx] != -1:      # 비어있는 칸이 아니고
#                             # if not visited[ny][nx]:     # 방문할곳에 방문한적 없다면
#                             if tomatoes[ny][nx] == tomatoes[ey][ex] + 1:
#                                 answer = tomatoes[ny][nx]
#                                 minus = 0
#                                 break
#                             tomatoes[ny][nx] = tomatoes[ey][ex] + 1
#                             # visited[ny][nx] = True
#                             q.append([ny, nx])
#
#
# print(tomatoes)
#
# answer = -1
# for i in range(n):
#     if 0 in tomatoes[i]:
#         answer = -1
#         break
#     answer = max(answer, max(tomatoes[i]))
#
# if answer < 0:
#     print(answer)
# else:
#     print(answer + minus)



from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append([nx, ny])


bfs()

for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res - 1)