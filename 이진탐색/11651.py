n = int(input())
arr = []

for i in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

arr = sorted(arr, key= lambda x: x[0])
arr = sorted(arr, key= lambda y: y[1])

for x in arr:
    print(*x)
