n = int(input()) # 도시 개수
p = list(map(int, input().split())) #리터당 가격
k = list(map(int, input().split())) #거리

total = 0
cost = p[0]

for i in range(n - 1):
    if cost > p[i]:
        cost = p[i]
    total += cost * k[i]
    
print(total)
