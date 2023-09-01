import sys
INF = int(1e9)

v, e = map(int, input().split())
k = int(input()) # 시작값

graph = [[] for i in range(v+1)]
visited = [False] * (v+1)
distance =[INF] * (v+1)

for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, v+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
    return index

def dijkstra(k):
    distance[k] = 0
    visited[k] = True

    for j in graph[k]:
        distance[j[0]] = j[1]

    for i in range(v-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
