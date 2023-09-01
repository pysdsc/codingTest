n = int(input())
nums = []

for i in range(n):
    k = int(input())
    if k == 0:
        nums.pop()
    else:
        nums.append(k)
        
print(sum(nums))
