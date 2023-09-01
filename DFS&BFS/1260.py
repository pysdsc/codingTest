from collections import deque
n, m, v = map(int, input().split())

graph = [[False] * (n + 1) for _ in range(n + 1)] # 여기 이해가 안 됨
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in range(1, n+1):
        if not visited[i] and graph[v][i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in range(1, n+1):
            if not visited[i] and graph[v][i]:
                queue.append(i)
                visited[i] = True

dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)
