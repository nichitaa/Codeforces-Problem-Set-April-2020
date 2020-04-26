'''Problem 3A - Shortest path of the king'''
# citim datele
s = str(input())
s1 = s[:1]
b = int(s[1:])
# am impartit tabla de sah in 8x8
# literi ii atribui valoarea din tabel
if s1 == 'h' : a = 8
if s1 == 'g' : a = 7
if s1 == 'f' : a = 6
if s1 == 'e' : a = 5
if s1 == 'd' : a = 4
if s1 == 'c' : a = 3
if s1 == 'b' : a = 2
if s1 == 'a' : a = 1
# la fel si pentru destinatie
t = str(input())
t1 = t[:1]
b1 = int(t[1:])
if t1 == 'h' : a1 = 8
if t1 == 'g' : a1 = 7
if t1 == 'f' : a1 = 6
if t1 == 'e' : a1 = 5
if t1 == 'd' : a1 = 4
if t1 == 'c' : a1 = 3
if t1 == 'b' : a1 = 2
if t1 == 'a' : a1 = 1

# aceiasi functie ca sii pentru afisarea miscarilor
# doar ca aici le numaram, si nu le afisam
def countthemerges(a,b,a1,b1):
    q = 0
    c = True
    while(c):
        if a < a1 and b > b1 :
            a = a + 1
            b = b - 1
            q+=1

        if a > a1 and b > b1:
            a = a -1
            b = b -1
            q+=1

        if a < a1 and b < b1:
            a = a +1
            b = b +1
            q+=1

        if a > a1 and b < b1 :
            a = a -1
            b = b +1
            q+=1

        if a == a1 and b > b1:
            b = b - 1
            q+=1

        if a == a1 and b < b1 :
            b = b + 1
            q+=1

        if b == b1 and a1 > a :
            a = a + 1
            q+=1

        if b == b1 and a > a1 :
            a = a - 1
            q+=1

        if a == a1 and  b1 == b :
            return q

# functie pentru afisarea miscarilor
def printthePosibitities(a,b,a1,b1):
    # iteram pana cand a e diferit de a1 si b de b1
    # algoritm de logica si matematica usoara
    # incrementam sau derementam valorile lui a si b
    # pana cand ele nu sunt egale cu a1 si b1
    # si respectiv la fiecare manipulare matimatica
    # afisam miscarea necesara
    c = True
    while(c):
        if a < a1 and b > b1 :
            print('RD')
            a = a + 1
            b = b - 1

        if a > a1 and b > b1:
            print('LD')
            a = a -1
            b = b -1

        if a < a1 and b < b1:
            print('RU')
            a = a +1
            b = b +1

        if a > a1 and b < b1 :
            print('LU')
            a = a -1
            b = b +1

        if a == a1 and b > b1:
            print('D')
            b = b - 1

        if a == a1 and b < b1 :
            print('U')
            b = b + 1

        if b == b1 and a1 > a :
            print('R')
            a = a + 1

        if b == b1 and a > a1 :
            print('L')
            a = a - 1

        if a == a1 and  b1 == b :
            c =False

# afisam numarul total de miscari
print(countthemerges(a,b,a1,b1))
# afisam miscarile
printthePosibitities(a,b,a1,b1)
