'''Problem 6B - President's Office'''

n,m ,s=input().split() # citim primul rand
n = int(n) # transformam in integer
m = int(m) #
a = [] # matricea n x m
for i in range(n):
    q = list(input()) # citim randul ca lista
    a.append(q) # si il adaugam in lista finala (matricea finala)

present = []
for i in range(n): # iterem in matrice
    for j in range(m):
        if a[i][j] == s: # daca gasim caractrul s, respectiv caracterul ce reprezinta masa presedintelui
            # verificam in toate directile posibile (rand + 1 , rand - 1 , coloana + 1, coloana - 1)
            # respectiv verificam dupa modelul:
            # unde X este masa presedintelui , iar 1 pozitile ce trebuiesc verificate,
            # daca pozitile 1 sunt diferite de X adaugam in lista [present]
            #                1
            #              1 X 1
            #                1
            #
            if i != 0 and a[i-1][j] != s: # daca indexul randului e diferit de 0 si caracterul de pe randul de mai jos
                                          # cu aceleasi coordinate j ( y ) e diferit de caracterul ce denota masa presedintelui
                                          # adaugam la raspuns
                present.append(a[i-1][j])
            if i != n-1 and a[i+1][j] != s: # daca nu este ultimul rand din matrice si daca caracterul din randul de mai sur
                                            # cu o unitate si aceiasi coordinate j ( y ) e diferit de caracterul ce denota masa
                                            # presedintelui adaugam la raspuns
                present.append(a[i+1][j])
            if j != m-1 and a[i][j+1] != s: # aceiasi logica si pentru coloane
                present.append(a[i][j+1])   # verificam doar decrementand si incremintand indexul j ( axa x a matricei)
            if j != 0 and a[i][j-1] != s:
                present.append(a[i][j-1])

helps = set(present) # transformam lista primita in multime
if '.' in helps:
    helps.remove('.') # si eliminam simbolul '.' , ce denota locurile libere
print(len(helps)) # afisam ranspunsul , lungimea multimii fara semnul '.'
