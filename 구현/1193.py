n = int(input())

line = 0    # 사선 라인
end = 0     # 입력된 숫자(input_num 변수)의 라인에서 가장 큰 숫자

while n > end:
    line += 1
    end += line

gap = end - n

if line % 2 == 0:     # 짝수 라인
    top = line - gap
    bottom = gap + 1
else:               # 홀수 라인
    top = gap + 1
    bottom = line - gap

print("%d/%d"%(top, bottom))
