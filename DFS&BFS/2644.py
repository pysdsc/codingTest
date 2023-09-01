n = int(input()) # 사람 수
a, b = map(int, input().split()) # 촌수 계산할 사람
m = int(input()) # 관계의 수

graph = [ [] for i in range(n + 1) ] # 그래프 초기화

for i in range(m): # 부모 자식 관계
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)

result = []
def dfs(v):
    cnt = 0
    visited[v] = True
    if v == b:
        return cnt
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(i)
    return cnt

if dfs(a) == 0:
    print(-1)
else:
    print(dfs(a))