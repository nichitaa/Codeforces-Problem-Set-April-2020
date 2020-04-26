'''Problem 3B - Lorry'''
n, v = map(int, input().split()) # citim nr de barci (katamarane si caiace) si capacitatea (volumul camionului)
baydarki, katamaran = [], []
for i in range(n):
    # formatul inputuli este :   1 capacitatea , sau
    #                            2 capacitatea
    # unde 1 semnifica ca utilajul e caiac , iar 2 - utilajul e catamaran
    t, p = map(int, input().split())
    # daca utilajul e caiac
    if t == 1:
        baydarki.append([p,i+1]) # adougam o lista de 2 elemente : [capacitatea_unitatii , indexul_acestei_unitati]
    # daca utilajul e catamaran
    else:
        katamaran.append([p,i+1]) # adougam in lista finala ,o lista ce descrie utilajul respectiv : [capacitatea, indexul]

baydarki.sort(reverse=True) # sortam dupa capacitatea unitatilor
katamaran.sort(reverse=True) #

load1, load2 = [0], [0]
capacity = 0 # capacitatea unui loadout
# daca avem mai mult spatiu in camion decat nr de caiace iteram prin toate caiacele,
# daca v este mai mic , iteram pana la v (precum 1 caiac ocupa 1 unitate din volumul camionului)
for i in range(min(v,len(baydarki))):
    capacity += baydarki[i][0] # pe rand adaugam capacitatea toatala a caiacelor
    load1.append(capacity) # obtinem lista de capacitati ale caiacelor , in dependenta de cate unitati folosim
capacity = 0
# aceiasi procedura si pentru catamarane
# doar ca tinem minte ca 1 catamaran ocupa 2 unitati din volumul camionului
# respectiv iteram pana volumul_camionului // 2 daca avem destule catamarane ,
# sau pana la nr_de_catamarane daca daca sunt mai putine ca v//2
for i in range(min(v//2, len(katamaran))):
    capacity += katamaran[i][0]
    load2.append(capacity) # obtinem lista de capactati a catamaranelor ,
    # in dependenta de nr de unitati luate ,( primele unitati sunt mereu cu capacitate mai mare)

# functie ce returneaza capacitatea cea mai buna pe care o putem incarca in camion si indexul la ce comvinatie
                                                                            # sa primit aceasta capacitate
def find_best_load():
    best = step = res = 0
    pos = min(v,len(baydarki))+1 # iteram pana la 1 + (v daca avem mai multe caiace, si pana la nr de caiace daca v este mai mare)
    for i in range(pos):
        kat_posibilities = int((v-i)/2) # nr de katamarane posibile sa punem in camaz la iteratia i
        # intrucat listele loadX sunt crescator ordonate pentru a extrage cea mai mare valoare posibila la iteratia i
        # aflam min de nr_de_catamarane si katamaranele_posibile_de_extras
        idx_best_katamarans = min(len(katamaran),kat_posibilities) # indexul katamaranululi cu cea mai mare capacitate,
        best = load1[i] + load2[idx_best_katamarans] # verificam best pentru toate combinatiile posibile
        if best > res: # actuaizam best si step daca obtinem o valoare mai mare
            res = best
            step = i
    return res, step # returnam valoarea maxima res, si iteratia la care sa obtinut aceasta valoare

# afisam solutile
def display_solution(r, step):
    print(r) # capacitatea maxima posibila pe care am obtinuto
    for i in range(step):
        print(baydarki[i][1], end=' ') # afisam indexul la caiace , cu valoarea maxima pana la iteratia step
    katamaran_range = min(len(katamaran), int((v-step)/2))
    for i in range(katamaran_range): # afisam indexul la catamarane , pana la (v-2)//2 intrucat ocupa 2 unitati
        print(katamaran[i][1], end=' ')

r, s = find_best_load() # aflam valoarea maxima pe care o putem incarca si pasul
display_solution(r, s)# afisam raspuns


'''
Un exemplu pe pasi

input :
10 10
1 14
2 15
2 11
2 12
2 9
1 14
2 15
1 9
2 11
2 6

Output:
baydarky  [[14, 6], [14, 1], [9, 8]]
katamaran  [[15, 7], [15, 2], [12, 4], [11, 9], [11, 3], [9, 5], [6, 10]]
load1  [0, 14, 28, 37]
load2  [0, 15, 30, 42, 53, 64]
------------
best  64              # ultimul element din load2
res  0
updated res  64
at step  0            # iteratia 0
------------
best  67              # 14 din load1 + 53 din load2 = 67, (4-katamarane, 1-baydarka)
res  64
updated res  67
at step  1
------------
best  81              # 28(load1) + 53(load2) = 81 , (2-baydarka, 4-katamaran) , ocupa maxim capacitate din v=10
res  67
updated res  81       # actualizat
at step  2            # actualizat
------------
best  79              # 47(load1) + 42(load2) = 79 , la fel ocupa capacitate v=10, insa suma este mai mica si nu actualizam res
res  81
81                    # raspunsul:
6 1 7 2 4 9
'''
