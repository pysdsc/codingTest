n = int(input()) # 사람 수
a, b = map(int, input().split()) # 촌수 계산할 사람
m = int(input()) # 관계의 수

graph = [ [] for i in range(n + 1) ] # 그래프 초기화

for i in range(m): # 부모 자식 관계
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
result = [0] * (n + 1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            result[i] = result[v] + 1 # 촌수가 올라갈 때마다 +1
            dfs(i)

dfs(a)
if result[b] > 0:
    print(result[b])
else:
    print(-1)