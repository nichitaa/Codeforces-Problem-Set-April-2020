'''Problem 14A - Letter'''
n,m = map(int,input().split(' ')) # citim nr de randuri si nr de caractere
r = []
for i in range(n):
    row = list(input()) # randul se salveaza ca o lista de caractere
    r.append(row) # in list r
first = []
last = []
f_row = []
for i in range(len(r)):
    for j in range(len(r[i])):
        # determinam prima si ultima pozitie a semnului *
        if r[i][j] == '*':
            f_row.append(i) # lista pentru randuri
            first.append(j) # lista pt start si end in index in rand

first_index = min(first) # start index pentru fiecare rand
last_index  = max(first) # end index pentru fiecare rand

f_row_idx = min(f_row) # incepem de la randul acesta
l_row_idx = max(f_row) # pana la ultimul rand
# afisam desenul final
for i in range(f_row_idx, l_row_idx+1):
    for j in range(first_index, last_index+1):
        print(r[i][j], end='')
    print()
