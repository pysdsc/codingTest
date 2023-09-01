n = int(input())
arr = [ input() for i in range(n) ]

result = list(set(arr)) # 중복 제거 단어
result.sort() # 알파벳순 정렬
result = sorted(result, key=len) # 길이순 정렬

for i in result:
  print(i)
