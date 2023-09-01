n = int(input())
p = list(map(int, input().split()))
sum = 0
p.sort()

for i in range(n):
    sum += n * p[i]
    n -= 1

print(sum)
