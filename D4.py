'''Problem 4D - Mysterious Present'''

from _bisect import bisect_left
# citim nr de plicuri , inaltimea si lungimea plicului original
n, w_plic, h_plic = map(int, input().split())
envs = [] # lista pentru caracteristicile fiecarui plic
for i in range(1,n+1): # citim lungimea si inaltimea fiecarui plic
    w, h = map(int, input().split())
    # adaugam lungimea si inaltimea fiecarui plic doar daca
    # lungimea si inaltimea lor este mai mare ca lungimea si inaltimea plicului original
    if w > w_plic and h > h_plic:
        # adaugam in lista envs w , h si indexul plicului
        # valoarea h (lungimea plicului) o adaugam ca valoare negativa
        # din considerenta ca vom sorta lista in ordine crescatoare dupa valorile w
        # si in ordine crescatoare dupa valoarea lui h , de exemplu: (lista deja sortata)
        # [[5002, -5005, 1], [5002, -5002, 5], [5002, -5001, 4], [5003, -5004, 2], [5003, -5002, 3]]
        # unde primul element al sublistei este w, al doilea h, si al treilea indexul i
        envs.append([w, -h, i])
if len(envs) < 1: print(0);exit() # daca lista nu contine plicuri mai mari ca plicul original , afisam 0
# sortam lista ce    contime doar combinatii valide
envs.sort()
#print(envs)
longest_subseq = [] # lista pentru a salva lungimea la plicurile ce vor forma cea mai lunga combinatie posibila
priority = [0] * len(envs) # initializam lista ce va contine ordinea aparitiei a plicului in lista de mai sus,
                           # la inceput toate el ement sunt netraversate si respectiv ordinea lor e 0
# iteram in lista de plicuri valide (cautam cel mai lung subsir)
for i in range(len(envs)):
    # setam inaltimea curenta (precul inaltimile au fost citite cu semnul minus, o transformam in valoare pozitiva)
    current_height = -envs[i][1]
    # daterminam pozitia in care trebuie sa punem lungimea in subsirul curent , astfel ca el sa ramanma sortat
    idx = bisect_left(longest_subseq,current_height)
    priority[i] = idx # actualizam ordinea aparitiei lungimei in subsirul curent
    # daca lungimea curenta e mai mica ca una din lungimile deja din subsirul curent
    if idx < len(longest_subseq):
        longest_subseq[idx] = current_height # inlocuim valoarea lungimii in subsir
    # daca lungimea curenta e cea mai mare din tot subsirul
    else:
        longest_subseq.append(current_height) # adaugam lungimea curenta in subsir

# initializam lista pentru a afisa raspunsul (una dintre cele mai lungi subsiruri)
res = [0]*len(longest_subseq)
print(len(longest_subseq)) # afisam lungimea celui mai lung sunbsir
order = len(longest_subseq) - 1 # initializam order ca indexul ultimului element in subsirul cel mai lung (plicul cel mai mare)
# iteram de la sfarsitul listei de plicuri
for i in range(len(envs)-1, -1, -1):
    # daca elementul cu valoarea maxima a indexului subsirului cel mai lung este egal cu order ( care la fel reprezinta pozitia plicul cel mai mare in cel mai lung subsir )
    if priority[i] == order:
        res[order] = (envs[i][2]) # adaugam la raspuns indexul plicului
        order -= 1 # trecem la urmatorul cel mai mare plic
print(*res, sep=' ') # afisam lista res (cu subsirul cel mai lung) intr-o linie
