'''Problem 9C - Hexadecimal's Numbers'''

n = int(input()) # citim numarul
s = 1 # incepem a cauta de la numarul 1
def bin_int(s):
    # pana cand numarul s in decimal e mai mic ca n :
    while ( int(bin(s)[2:]) <= n): # functia bin() returneaza valoarea in binar in felul
                                   # in felul urmator : decimal 10 = 0b1010 in binar
                                   # pe noi ne intereseaz doar valoarea 1010 , respectiv
                                   # taiem lista de la al 2 index : [2:]
        return bin_int(s + 1)      # returnam recursiv s + 1 , pana cand nr s din binar convertit
                                   # in decimal e mai mic ca nr n
    return s - 1 # retrunam raspunsul s-1 (precum am inceput de la s = 1)
                 # care si reprezinta nr total de numere binare de la 1 la n
print(bin_int(s)) # afisam raspunsul
