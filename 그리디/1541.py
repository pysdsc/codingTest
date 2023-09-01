exp = input().split("-") # - 기준으로 식을 나눔 ex) 4, -, 5+3, -
sum = []

for i in exp:
    s = 0
    tmp = i.split("+") # + 기준으로 exp 원소를 나눔
    for j in tmp:
        s += int(j) # 나눠진 원소끼리 더함
    sum.append(s) # 더한 것들의 총합
    
result = sum[0]
for i in range(1, len(sum)):
    result -= sum[i]
    
print(result)
