'''Problem 10B - Cinema Cashier'''

# gasim toate locurile posibile
def find_avaible(size):
    pos = []
    for i in range(k): # iteram pe randuri
        j = c = 0
        while j < k: # cautam subsirul ne zerouri de lungime size
            # daca locul e liber:
            if th[i][j] == 0:
                c += 1 # incrementam counterul
                if c == 1: # daca counterul e 1 :
                    start = j # salvam pozitia de start
                # daca counterul e egal cu lungimea necesara:
                if c == size:
                    end = j # salvam pozitia finala
                    # adaugam in lista datele, dupa forma:
                    # [nr randului, prima coloana , ultima coloana] (pentru m=size locuri consecutive)
                    pos.append([i+1, start+1, end+1]) # adaugam in lista
                    j = start + 1 # incepem a cauta de la indexul de start al subsir precedent
                    c = 0 # counter = 0
                else:
                    j+=1 # actualizam j
            # daca locul e ocupat ( != 0) :
            else :
                j+=1 # actualizam j
                c = 0 # setam counterul egal cu 0
    # daca nu au fost gasite m=size locuri consecutive in nici un rand:
    if len(pos) == 0:
        return -1 # returnam -1
    # returnam toate posibilitatile gasite
    else:
        return pos
# gasim m locuri consecutive cu distanta ce mai mica pana la centru
# parametrii : ok = lista bidimensionala de toate m locuri consecutive
              # size = m locuri consecutive
def closest(ok, size):
    dists = [] # lista pentru a salva toate distantele
    for i in range(len(ok)):
        d = find_dist(ok[i], i) # distanta pentru posibilitate i (pentru subsirului i)
        dists.append(d) # o adaugam in lista

    # sortam toate crescator distantele dupa atributele urmatoare : 1. distanta generala pana in centru 2. randul 3. coloana
    dists.sort(key = lambda x: (x[0], x[1], x[2]))
    # dupa sortare primul element in lista va avea cele trei atribute cu valoare minima
    print(*ok[dists[0][3]], sep= ' ') # il afisam

    # locurile care au fost afisate le inlocuim cu 1
    for i in range(ok[dists[0][3]][1]-1, ok[dists[0][3]][2]):
        th[ok[dists[0][3]][0]-1][i] = 1

# calculam distanta dupa formula
# suma (de la prima coloana din subsir -> pana la ultima coloana din subsir) = | randul subdirului - randul central| + | coloana curenta - coloana centerala |
def find_dist(arr, idx):
    d = 0
    for i in range(arr[1], arr[2]+1):
        d += abs(arr[0]-center) + abs(i - center) # calculam distanta generala pana in locul din centru
    # returnam :
    # [distanta generala, randul subsirului, prima coloana a subsirului]
    return [d, arr[0], arr[1], idx]



n ,k = map(int, input().split()) # citim nr de subsiruri , si dimensiunile matricii
m = list(map(int, input().split())) # citim lungimile pentru fiecare subsir

r = c = k
th = [[0 for x in range(r)] for y in range(c)] # creem o matrice kxk de zerouri

center = (k+1) // 2 # determinam locul din centru
# iteram in lista cu lungime pentru fiecare m locuri consecutive
for i in range(len(m)):
    p = find_avaible(m[i]) # determinam toate posibilitatile pentru m[i] locuri consecutive
    if p == -1: # daca nu sunt posibilitati
        print(-1) # afisam -1
    # daca sunt mai multe posibilitate:
    else:
        closest(p , m[i]) # afisam subsirul cu distanta minima de la centru
