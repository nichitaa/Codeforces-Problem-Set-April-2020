'''Problem 5B - Center Alignment'''

import sys
inputList = [k.strip() for k in sys.stdin] # citim randurile din stdin si le salvam in liata
maxLength = max(len(a) for a in inputList) # determinam randul cu cele mai multe caractere

print((maxLength + 2) * '*') # afisam primul rand de '*' (cu doua caractere in plus , pentru margini)

now = 1 # flag penru a schimba pe rand orientarea la spatii libere in caz ca nu sunt destule
for row in inputList:
    # nr de spatii care trebuie afisate
    spaces = maxLength - len(row)
    if spaces % 2 : # daca nr de spatii ce trebuie afisate e impar
        # in acest caz alternam pozitia spatiilor
        # incepem cu stanga (dupa conditie)
        if now == 1:
            now = 0 # schimbam flagul pt iteratia urmatoare
            # afisam randul cu semnul '*' la inceput si sfarsit
            print('*{text} *'.format(text=row.center(maxLength-1, ' ')))
        # spre dreapta
        elif now == 0:
            now = 1 # schimbam flagul pt iteratia urmatoare
            print('* {text}*'.format(text=row.center(maxLength-1, ' ')))
    # daca sunt destule spatii libere afisam randul centrat
    else:
        print('*{text}*'.format(text=row.center(maxLength, ' ')))
# afisam ultimul rand de seme '*'
print((maxLength + 2) * '*')
