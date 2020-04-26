'''Problem 1B - Spreadsheet'''

import re
# functie pentru a converti din caracter in numar (dupa formul ascii)
def to_int(s):
    r = 0
    for i in s:
        r = r*26 + (ord(i) - ord('A') + 1)
    return r # returneaza int
# functie pentru a converti din numar in caracter
def to_str(n):
    s = ''
    while n != 0:
        n -= 1
        s += chr( n%26 + ord('A'))
        n //= 26
    return s # returnam stingul s (el trebuie reversat a obtine ordinea corecta a coloanei)

n = int(input()) # citim nr de randuri
pattern = 'R(\d+)C(\d+)' # paternul pentru a verifica din ce categorie face parte sirul din input ( avem doar 2 variante distincte)
# paternul respectiv este pentru (R+integer+C+integer) , untde R - row, C - column
res = [] # lista cu toate raspunsurile salvate
for i in range(n):
    s = str(input()) # citim randul
    if (re.match(pattern, s)) != None: # daca face parte din paternul descris mai sus
        for i in range(len(list(s))): # gasim indexul la caracterul 'C'
            if list(s)[i] == 'C': idx = i
        n1 = s[1:idx] # n1 = numarul din fata caracterului 'R'
        n2 = int(s[idx+1:]) # n2 = numarul din fata caracterului 'C'
        wor = to_str(n2) # # wor = transformam in string
        new = wor[::-1] # inversam wor
        res.append(new+n1) # adaugam la raspuns concatinarea intre stingul creat si numarul randului (pt R)
    # in caz ca e alt pattern
    else :
        for i in range(len(list(s))): # gasim indexul la prima cifra , care va reprezenta in
            if list(s)[i].isdigit():
                idx = i
                break
        # separam caracterele pentru a afla randul si coloana
        wor = s[:idx] # wor = stringul pana la prima cifra
        num = int(s[idx:]) # numarul randului ce trebuie afisat
        col = to_int(wor) # trssformam coloana din string in integer
        c1 = str(col) # convertim in string pentru a putea concatina valorile la raspuns
        nr = str(num)
        foo = ('R%sC%s' %(nr,c1)) # rasupunsul concatinat
        res.append(foo) # adaugam raspunsul in lista finala
# afisam lista de raspunsuri
for i in range(len(res)):
    print(res[i])
