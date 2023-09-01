import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

m = int(input())
arr2 = list(map(int, input().split()))

def binary_search(target):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if arr1[mid] == target:
            return True
        if target < arr1[mid]:
            end = mid - 1
        elif target > arr1[mid]:
            start = mid + 1

for i in range(m):
    if binary_search(arr2[i]):
        print(1)
    else:
        print(0)