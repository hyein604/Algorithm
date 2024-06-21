from collections import deque
n, m, v = map(int, input().split())     # 정점 개수, 간선 개수, 시작할 정점 번호
table = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    table[a].append(b)
    table[b].append(a)
for i in range(n+1):
    table[i] = sorted(table[i])

# dfs
visit_dfs = [False for _ in range(n+1)]
def dfs(idx):
    print(idx, end=' ')
    visit_dfs[idx] = True

    for i in table[idx]:
        if not visit_dfs[i]:
            dfs(i)


dfs(v)
print()

# bfs 1 2 3 4
visit_bfs = [False for _ in range(n+1)]
q = deque()
q.append(v)

while q:
    node = q.popleft()
    print(node, end=' ')
    visit_bfs[node] = True

    for tmp in table[node]:
        if not visit_bfs[tmp]:
            visit_bfs[tmp] = True
            q.append(tmp)