'''Problem 4A - Watermelon'''
w = int(input())
# verificam daca putem scadea 2 din w si daca nr ramas este par pt a satisface conditiile
if (w-2)%2 ==0 and w-2 >= 2:
    print('YES') # afisam raspunsul 
else: print('NO')
