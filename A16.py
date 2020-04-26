'''Problem 16A - Flag'''
n,m=map(int,input().split()) # citim n si m
flag = []
for i in range(n):
    row = str(input())
    r = list(row) # transformam randul introdus intr-o lista
    flag.append(r) # lista creata o adaugam la lista flag
c = 0
# in caz ca flagul e doar dintrun rand
if len(set(flag[0]))!=1:
    c=1
# in caz ca flagul are 2 elemnte
if len(flag)>1 and set(flag[0]) == set(flag[1]) :
    c = 1
# verificam pana la flag-1 raduri
for i in range(len(flag)-1):
    # daca multimea unui rand e diferita de 1 , inseamna ca avem mai multe
    # culori , ceea ce e interziz
    if (len(set(flag[i]))!=1):
        c = 1
        break
    # daca multimea de numere a randului curent este egala cu multimea randuli
    # urmator , ceea ce nu indeplineste conditia , setam c = 1
    if set(flag[i]) == set(flag[i+1]):
        c= 1
        break
# verificam ultima coloana
if (len(set(flag[-1])))!=1:
    c = 1

# afisam raspunsul
if c == 0: print('YES')
else: print('NO')
