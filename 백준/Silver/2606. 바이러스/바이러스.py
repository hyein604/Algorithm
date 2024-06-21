n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

# 그래프 만들기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def recur(node):
    visit[node] = 1

    for nxt in graph[node]:
        if visit[nxt] == 1:
            continue
        recur(nxt)

recur(1)
print(sum(visit)-1)