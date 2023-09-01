N, K = map(int, input().split())
coin = []
count = 0

for i in range(N):
   coin.append(int(input()))

for i in reversed(range(N)):
   if K == 0:
      break   
   if coin[i] > K:
      continue
   count += K // coin[i]
   K %= coin[i]
   
print(count)
