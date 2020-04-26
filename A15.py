'''Problem 15A - Cottage Village'''
n,t = map(int,input().split(' ')) # citim nr. total de case , si t - lungimea laturii casei noi
all_houses = []
for i in range(n):
    house_i = list(map(int, input().split())) # datele pt fiecare casa le salvam fieacare in lista separata
    all_houses.append(house_i) # adaugam datele pentru casa_i in lita cu toate casele
all_houses.sort(key=lambda x:x[0]) # sortam lista cu toate casele , dupa centrul caselor , adica dupa
                                                            # primul element din fiecare sublista

p = 0 # variabila pentru a salva toate posibilitatile de amplasare a casei vu latura t
for i in range(n-1): # iteram pana la penultima casa
    # determinam pozitia pentru peretele drept al casei i , stiind centrul casei
    # dupa formula : r_x = (lungimea casei / 2) + centrul casei
    r_x = (all_houses[i][1] / 2 ) + all_houses[i][0]
    # determinam pozitia pentru peretele stang al casei i+1
    # dupa formula : l_x = centrul casei - (lungimea casei / 2)
    l_x = all_houses[i+1][0] - (all_houses[i+1][1] / 2 )
    # daca diferenta intre aceste doua valori e mai mare ca latura t
    # respectiv avem inca 2 posibilitati de a construi casa ( conectata de casa i, sau de casa i+1)
    if l_x - r_x > t:
        p+=2
    # daca diferenta e egala cu lungimea t a casei , respectiv avem doar o posibilitate de amplasare
    # ( conectata de ambele case, i si de i+1 )
    elif l_x - r_x == t:
        p+=1
# intrucat mai avem inca doua posibilitati de amplasare pentru casa cu latura t
# ( lipita de peretele stang al primei case sau lipita de peretele drept al ultimei case )
# afisam raspunsul adaugand aceste 2 posibilitati
print (p+2)
