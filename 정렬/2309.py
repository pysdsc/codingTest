arr = []

for i in range(9):
    n = int(input())
    arr.append(n)

arr.sort()

total = sum(arr)

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if total - arr[i] - arr[j] == 100:
            for k in range(len(arr)):
                if k == i or k == j:
                    pass
                else:
                    print(arr[k])
            exit()

