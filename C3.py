'''Problem 3C - Tic-tac-toe'''

a = input()  # citim matricea , fiecare rand in lista aparte
b = input()
c = input()
nrOfX = (a+b+c).count('X') # nr toatal de X-uri ce se intalneste in matrice
nrofZ = (a+b+c).count('0') # nr total de zerouri ce se intalneste in matrice
difference_ofSteps = nrOfX-nrofZ # diferenta lor (tinem in minte ca X-ul merge primul)
                                 # daca aceasta diferenta este mai mare ca 1 , respectiv joaca e ilegala

full_game = [] # lista pentru a adauga toate combinatiile posibile din matrice
full_game.append(a) # adaugam randul 1
full_game.append(b) # adaugam randul 2
full_game.append(c) # adaugam randul 3
full_game.append(a[0]+b[1]+c[2]) # adaugam diagonala 1
full_game.append(a[2]+b[1]+c[0]) # adaugam diagonala 2
full_game.append(a[0]+b[0]+c[0]) # adaugam coloana 1
full_game.append(a[1]+b[1]+c[1]) # adaugam coloana 2
full_game.append(a[2]+b[2]+c[2]) # adaugam coloana 3

# verificam cine a castigat , variabila both_won va lua valori de la 0 la 2
both_won = ('XXX' in full_game) + 2*('000' in full_game) -1

# daca diferenta dintre pasi este negative sau mai mare ca 1 : illegal
# sau daca au fost gasite 'xxx' si '000' in lista full_game  : illegal
# sau daca diferenta dintre x si zerouri este egala cu castigul lui primul jucator sau al doilea
# explicatie : daca diferenta dintre X-uri si zerouri este 0, respectiv doar jucatorul al doilea
# poate sa castige , iar daca diferecta este 1 , ceea ce inseamna ca jucatorul X (primul) a facut
# cu un pas mai mult si doar el poate sa castige , sau deja sa fie egalitate, daca niciunul nu a castigat
if (difference_ofSteps not in (0,1)) or both_won > 1 or difference_ofSteps==both_won :
    print('illegal')

# daca a fost gasita combinatia 'xxx' in full_game : primul jucator a castigat
elif 'XXX' in full_game:
    print('the first player won')

# daca a fost gasita combinatia '000' in full_game : al doilea jucator a castigat
elif '000' in full_game:
    print('the second player won')

# daca nici unul din jucatori nu a castigat si nu mai avem spatii libere (de semnul '.') : egalitate
elif nrOfX+nrofZ == 9:
    print('draw')

# daca jucatorii inca mai au spatii libere : afisam ca jucator trebuie sa mearga
else :
    next_turn = ["first", "second"]
    print(next_turn[difference_ofSteps])
