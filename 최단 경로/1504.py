import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [ [] for i in range(n+1) ]
INF = int(1e9)

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

v1, v2 = map(int, input().split())

def f(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

dist_1 = f(1) # 1 -> n까지
dist_v1 = f(v1) # v1 -> n까지
dist_v2 = f(v2) # v2 -> n까지

result = min(dist_1[v1] + dist_v1[v2] + dist_v2[n], dist_1[v2] + dist_v2[v1] +dist_v1[n])
print( result if result < INF else -1)



