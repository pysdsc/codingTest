c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
n = input()
for i in c:
    n = n.replace(i, 'a') # replace는 문자열에서 어떠한 값을 찾아 변경해 주는 역할
print(len(n))
