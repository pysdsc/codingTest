n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

result = [0] * m

for i in range(m):
    for j in range(n):
        if arr2[i] == arr1[j]:
            result[i] += 1
        else:
            continue

for i in result:
    print(i)


