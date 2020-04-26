'''Problem 13A - Numbers'''
# functie ce va converti numarul in baza: base
# si va returna suma cifrelor numarul convertit
def convert_base(number, base):
    if base < 2:
        return False
    remainders = []
    while number > 0:
        # salvam cifrele numarului convertit in baza noua ,in lista remainders
        remainders.append(int(number % base))
        number //= base
    return sum(remainders) # returnam suma listei

num = int(input())
gd = num-2 # numitorul (nr total de baze in care a fost convertit numarul)
i = 2
res = 0 # suma totala
# aflam suma totala a cifrelor numarului in toate bazele de la 2 pana la n-1
while i != num:
    res += convert_base(num, i)
    i += 1
# simplificam numitorul si numaratorul
for i in range(2, res):
    while res % i == 0 and gd%i ==0 :
        res /= i
        gd /= i
# afisam ca fractie simplificata
print('%d/%d' %(res,gd))
