n = int(input())
nums = []

for i in range(n):
    x = int(input())
    nums.append(x)

sum = 0

for i in range(n):
    if nums[i] == 0:
        nums.pop(i-1)
    else:
        sum += nums[i]

print(sum)
        
        

