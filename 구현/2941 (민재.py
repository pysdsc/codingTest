word = input()
c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#ljes=njak
cnt = 0
for a in c_alpha:
    if a in word:
        cnt += word.count(a)
        word = word.replace(a, "")     #_e__ak
        
    else:
        continue

cnt += len(word)

print(cnt)
