'''Problem 4B - Before an Exam'''
d, summ = map(int, input().split()) # citim nr de zile si suma totala
mintime, maxtime = [], []
for i in range(d):
    mi, mx = map(int, input().split()) # mi = timpul minim pentru ziua i, si respectiv mx = timpul maxim pentru ziua i
    mintime.append(mi) # salvam toate timpurile minimale in mintime
    maxtime.append(mx) # salvam toate timpurile mazimale in lista maxtime

min_sum = sum(mintime) # aflam timpul minim posibil pe care baiatul putea sal petreaca invatand
max_sum = sum(maxtime) # aflam timpul maxim posibil pe care baiatul putea sal petreaca invatand
# daca suma minima totala e mai mare ca suma necesara totala sau daca suma totala necesara este mai mare ca suma maxima
# afisam raspunsul negativ
if min_sum > summ or summ > max_sum :
    print('NO')
else:
    res = mintime[:] # copiem lista timpului minim pe care baiatul putea sal petreaca invatand in lista res (raspuns)
    # iteram pe zile
    for i in range(d):
        if sum(res) == sum : break # in caz ca suma din res e suficienta , oprim iteratia
        # daca suma din res nu corespunde sumei necesare
        else:
            # pana cand res[ ziua i ] e diferit de timpul maxim pe care baiatul putea sal petreaca invatand
            while(res[i]!=maxtime[i]):

                if sum(res)==summ: # verificam daca avem suma necesara, daca da:
                    break # oprim
                # adaugam inca o ora la res[ ziua i]
                res[i]+=1
    # afisam raspunsul si toata lisya intr- un rand
    print('YES')
    print(*res)
