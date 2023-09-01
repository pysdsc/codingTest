n = int(input())
r = []

for i in range(n):
    s,e = map(int, input().split())
    r.append([s, e])

r.sort(key=lambda x:(x[1], x[0])) # 종료시간 정렬 후, 시작시간 정렬 

end = r[0][1] # 가장 빨리 끝나는 회의
cnt = 1 # end 회의를 포함하고 카운트 시작

for i in range(1, n):
    if r[i][0] >= end:
        cnt += 1
        end = r[i][1]

print(cnt)
