from collections import deque

n, m = map(int, input().split())    # 세로, 가로
paper = [list(map(int, input().split())) for _ in range(n)]
visit = [[False for _ in range(m)] for _ in range(n)]   # 방문 기록용
maxi = 0
picture_count = 0

for i in range(n):  # 세로좌표
    for j in range(m):  # 가로좌표
        if paper[i][j] == 1 and visit[i][j] == False:   # 그림이고, 방문한적 없다면
            picture_count += 1
            # bfs
            q = deque()
            q.append([i, j])
            visit[i][j] = True
            area = 1
            
            while q:
                ey, ex = q.popleft()

                # 4방향 탐색
                for dy,dx in [0, 1], [0, -1], [1, 0], [-1, 0]:  #우, 좌, 하, 상
                    ny = ey + dy    # 갈곳의 y 좌표
                    nx = ex + dx    # 갈곳의 x 좌표

                    if 0 <= ny < n and 0 <= nx < m:     # 갈곳이 종이 범위 안이라면
                        if paper[ny][nx] == 1:          # 갈곳이 그림이라면
                            if not visit[ny][nx]:       # 갈곳에 방문한적 없다면
                                visit[ny][nx] = True
                                area += 1
                                q.append([ny,nx])
                                
            maxi = max(maxi, area)

print(picture_count)
print(maxi)