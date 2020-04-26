'''Problem 7B - Memory Manager'''

t, m = map(int, input().split()) # citim nr de comenzi si nr total de biti
ops = [] # lista pentru a salva comenzile
m = [0]*m # un block continuu de memorie , (0 - pentru biti liberi , 1 - pentru biti folositi)
blocks = dict() # dictionar pentru a salva fiecare operatie de alloc in forma:
                    # <identificator> : [primul_bit , ultimul_bit]
# citim toate comenzile
for i in range(t):
    op = list(input().split())
    if len(op) > 1: # daca inputul contine 2 elemente :
        # avem operatia de alloc n biti sau erase indetificator_x
        nr = int(op[1]) # convertim nr de biti in integer
        ops.append([op[0], nr]) # adaugam ca o sublista operatia curenta in lista cu toate operatile
    # daca inputul e din un element : avem operatia de defragmentare
    else:
        ops.append([op[0]]) # o adaugam in lista cu operatii

# functia de allocare a memoriei
# parametri de intrare : idnf - identificator( unic ) pentru fiecare bloc de memorie alocat
                    # size - marimea blocului de memorie ce trebuie alocat
def alloc(indf ,size):
    global m, blocks
    c = 0 # variabile pentru a afla primul si ultimul bit al blocului de memorie allocat
    for i in range(len(m)): # iteram in lista de memorie (m)
        if m[i] == 0: # daca gasim un bit 0
            c += 1     # actualizam c
            if c == 1: # daca c e initializat ca 1, respectiv incepem a numara nr de biti ce trebuie allocati
                str_idx = i # si salvam indexul primului bit din memorie ce va fi allocat in caz ca blocul e
                            # e destul de lung
        # daca intalnim in memorie bitul 1 :
        if m[i] == 1:
            c = 0 # incepem a cauta alt bloc in memorie
        # daca c este egal cu marimea blocului ce trebuie alocat :
        if c == size:
            end_idx = i # salvam ultimul index al blocului curent
            # alocam memorie
            # pentru blocul cu start index si end index + 1 , inlocuim in memorie bitii de 0 cu bitii de 1
            for i in range(str_idx, end_idx+1):
                m[i] = 1
            # salvam operatia in dictionar sub forma:
            # <identificatorul blocului alocat> : [primul index al blocului alocat, ultimul index al blocului alocat]
            blocks[indf] = [str_idx, end_idx+1]
            # returnam True, precum operatia a fost efectuata cu succes
            return True
    # returnam False , daca nu sa putut aloca memorie
    return False

# functie pentru operatia de erase
# parametru de intrare :indf - identificator al blocului ce trebuie de eliminat din memorie
def erase(indf):
    global m, blocks
    # iteram in dictionar ( in toate blocurile alocate )
    for indetificators , indexes in blocks.items():
        # daca gasim identificatorul blocul caruia trebuie dealocat
        if indetificators == indf:
            # dealocam memoria ( biti de 1 ii inlocuim cu bitii de 0)
            # incepand de la primul index al blocului pana la ultimul
            for i in range(indexes[0], indexes[1]):
                m[i] = 0
            # eliminam blocul dealocat din dictionar
            del blocks[indf]
            # return True , pentru operatia de succes
            return True
    # returnam False in caz nu sa putut dealoca momorie
    return False

# functia pentru operatia de defragmentare
def defragment():
    global m , blocks
    end_block = 0
    # iteram in dictionar ( toate blocurile de memorie alocata )
    for idf, idx in blocks.items():
        # nr de biti ce trebuie defragmentati :
        # size = ultimul index al blocului - primul index al blocului
        size_realloc = idx[1] - idx[0]
        # dealocam blocul curent
        for i in range(idx[0], idx[1]):
            m[i] = 0 # setam blocul curent ca un bloc liber
        # realocam blocul curent
        # ( il aducem in fata memoriei )
        alloc(idf, size_realloc)

alloc_list = [0] # lista pentru a salva idenificatorii pentru fiecare bloc de memorie
for i in range(len(ops)):
    # daca e operatia de memorie
    if ops[i][0] == 'alloc':
        # determinam identificatorul petru blocul nou de memorie
        idnnf = max(alloc_list)+1
        # daca operatia de alocare a fost efectuata cu succes
        if alloc(idnnf , ops[i][1]):
            print( idnnf) # afisam identificatorul
            alloc_list.append(idnnf) # si il adaugam in lista
        # daca operatia de alocare a esuat
        else:
            print('NULL') # afisam mesajul de erroare
    # pentru operatia de erase:
    elif ops[i][0] == 'erase':
        # daca operatia erase a esuat :
        if erase(ops[i][1]) == False:
            print('ILLEGAL_ERASE_ARGUMENT') # afisam mesajul de erroare
    # pentru operatia de defragmentare:
    elif ops[i][0] == 'defragment':
        # defragmentam toata memoria
        # aducem bitii de 1 ai fiecarui bloc , la inceputul memorie , respectand consecutivitatea identificatorilor
        defragment()
