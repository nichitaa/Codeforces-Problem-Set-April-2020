'''Problem 6C - Alice, Bob and Chocolate'''

n = int(input()) # citim nr. de ciocolate
l = list(map(int, input().split())) # citim timpul pentru fiecare ciocolata
a = l[0] # alice incepe de la prima ciocolata
b = l[-1] # bob incepe de la ultima ciocolata
i = 1 # precum deja am setat valori lui a si b, incepem de la 1 si n-2
j = n - 2
while i<=j: # pana cand nu mai sunt ciocolate
    # daca ciocolata lui bob are timpul mai mic
    if a > b:
        b += l[j] # trecem la ciocolata urmatore, actualizand timpul b
        j -= 1
    # daca ciocolata lui bob are timpul mai mare sau egal decat ciocolata (ciocolatele)
    # lui alice
    else:
        a += l[i] # alice trece la ciocolata urmatoare , actulizand timpul a
        i += 1
# precum alice a inceput din partea stanga spre dreapta afisam pana la ce
# ciocolata a ajuns alice ,si ciocolatele ramase , respectiv pe care le-a mancat bob
print(i, n-i)
