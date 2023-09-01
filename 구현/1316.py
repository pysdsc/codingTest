n = int(input())

for i in range(n):
    word = list(input())
    for j in range(len(word)-1): # index는 0부터,len()은 1부터 -> -1
        if word[j] == word[j+1]:  # 연속되는 알파벳이 겹치는지 검사
            pass
        elif word[j] in word[j+2:]:# 이미 등장했던 알파벳이 연속되지 않게 등장
            n -= 1
            break
print(n)
