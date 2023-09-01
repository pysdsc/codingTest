n = int(input())
slist = []
rank = []
for i in range(n):
    x, y = map(int, input().split())
    slist.append([x, y])

for i in range(n):
    cnt = 0
    for j in range(n):
        if slist[i][0] < slist[j][0] and slist[i][1] < slist[j][1]:
            cnt += 1
    rank.append(cnt+1)

for i in range(n):
    print(rank[i], end = " ")
