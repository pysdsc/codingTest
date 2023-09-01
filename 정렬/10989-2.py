import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    a = int(input())
    arr.append(a)

count = [0] (max(arr) + 1)

for i in range(len(arr)):
    count[arr[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = '/n')
