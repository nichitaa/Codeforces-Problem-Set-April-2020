'''Problem 8B - Obsession with Robots'''
path = input() # citim calea robotului

# functia acesta va returna pozitia noua a punctului (x, y)
# in dependenta de ce caracter i se transmite (argumentul pos)
def moves(c, pos):
    if pos == 'R':
        return (c[0]+1, c[1])
    if pos == 'L':
        return (c[0]-1, c[1])
    if pos == 'U':
        return (c[0], c[1]+1)
    if pos == 'D':
        return (c[0], c[1]-1)

def correct(path):
    l = list(path) # transformam calea dintr-un sir, intr-o lista
    c = (0,0) # setam primul punct ca (0, 0) (x, y)
    p = None # variabila ce va desemna punctul anterior in path
    all = set() # multimea pentru a adauga punctele dupa fiecare iteratie
    all.add(c)  # adaugam primul punct (0, 0)
    # iteram in lista path
    for i in range(len(l)):
        n = moves(c, l[i]) # aflam n = pozitia_urmatoare a punctului in dependenta
                           # de ce caracter intalnim in path
        # in caz ca pozitia anterioara si curenta sun la fel , ex : RL, LR , DU, UD
        if n == p : return False # returnam false
        p = c # poz_anterioara = poz_curenta
        c = n # poz_curenta = poz_urmatoare
        all.add(c) # adaugam la multime
        flag = 0
        # verificam daca formeaza ciclu :
        mov = ['R', 'L', 'U', 'D'] # toate cazurile posibile de pasuri
        for i in range(len(mov)):
            if moves(c, mov[i]) in all : # daca pozitia punctului_curent in toate directile
                                        # deja se afla in multime , incrimentam flag
                flag +=1
        if flag > 1:                    # daca flag > 1 , atunci formeaza un ciclu, si returnam false
                return False
    return True #daca nici o conditie de mai sus nu au fost satisfacute returnam true

if correct(path): print('OK'); exit() # transmitem la functia correct , sirul de caractere - path
                                      # si daca valoare returnata e true afisam 'OK'
# afisam mesajul respectiv daca valoarea returnata e false
else : print('BUG'); exit()
