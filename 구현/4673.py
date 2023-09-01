nums = list(range(1, 10001))
remove_list = []

for i in nums:
    for j in str(i):
        i += int(j)
        
    if i <= 10000:
        remove_list.append(i)

for i in set(remove_list):  # set으로 중복값 제거
    nums.remove(i)  # remove: 값을 입력하여 삭제
    
for selfnum in nums:
    print(selfnum)
