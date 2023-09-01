n = input()
cnt = 0

for i in range(n):
    if n[i] == 'c':
        if n[i+1] == '=' or n[i+1] == '-':
            cnt += 1
    elif n[i] == 'd':
        if n[i+1] == '-' :
            cnt += 1
        elif n[i+1] == 'z' and  n[i+2] == '=':
            cnt += 1
    elif n[i] == 'l' or n[i] == 'n':
        if n[i+1] == 'j':
           cnt += 1
    elif n[i] == 's' or n[i] == 'z':
        if n[i+1] == '=':
           cnt += 1

    if n[i] in alphabet:
        cnt += 1
        
    

print(cnt)
