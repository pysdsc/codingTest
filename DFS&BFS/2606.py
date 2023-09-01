from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)] # 여기 이해가 안 됨 (그래프 초기화)
visited = [False] * (n + 1)

for _ in range(m): # 그래프 생성
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    count = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == False: # 방문하지 않았다면
                queue.append(i)
                visited[i] = True # 방문 처리
                count += 1
    return count

print(bfs(graph, 1, visited))