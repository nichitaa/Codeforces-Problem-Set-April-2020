'''Problem 7A - Kalevitch and Chess'''
c = 0
r = 0
k = 0
for _ in range(8): # matrice 8x8
    n = input() # citim sirul
    if n == 'BBBBBBBB': c += 1 # daca e format doar din B , adaugam la raspun + 1 coloana
    else:
        for i in n: # verificam cati de B avem intr-un rand, pentru fiecare rand diferit de 'BBBBBBBB'
            if i == 'B':
                r += 1 # actualizam nr. total de B-uri in siruri
        k += 1 # actualizam nr total de randuri diferite de 'BBBBBBBB'
if k == 0: print(8) # in caz ca avem doar randuri de 'BBBBBBBB'
# folosim formula pentru a calcula nr total de randuri sau coloane de 'BBBBBBBB'
else :  print(c + r//k)
