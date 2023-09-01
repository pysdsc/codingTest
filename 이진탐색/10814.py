n = int(input())
arr = []

for i in range(n):
    data = input().split()
    arr.append((int(data[0]), data[1]))

arr = sorted(arr, key=lambda user: user[0])

for user in arr:
    print(*user)