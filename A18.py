'''Problem 18A - Triangle'''
import  math
a1,a2,b1,b2,c1,c2 = map(int, input().split()) # citim coordinatele punctelor

# functie ce verifica daca laturile unui triunghi formeaza un triunghi dreptunghic
def is_triangle(ip,c1,c2):
    if c1 == 0 or c2 == 0 : return False # in caz ca una din catete are lungime egala cu zero
    # folosim trunc pentru a scapa de erroarea in calculul radicalului din teorema lui pitagora
    # retutunam valoarea booleana respectiva (True sau False)
    return math.trunc(ip*100000)/100000 == math.trunc(math.sqrt(pow(c1,2) + pow(c2,2))*100000)/100000

# functie ce calculeaza lungimile laturiloe dupa punctele lor pe axa
# ca argument i se transmite o lista , elementele careia sunt 0,1 si -1, pentru a putea calcula lungimile
# laturilor cu punctele diferite de o unitate
def pitagora_th(n=[0]*6):
    # in fiecare formula punctele de la input se aduna cu elementele listei n
    ab = math.sqrt((a1 + n[0] - (b1 + n[2]))**2 + (a2 + n[1] - (b2 + n[3]))**2)
    bc = math.sqrt((b1 + n[2] - (c1 + n[4]))**2 + (b2 + n[3] - (c2 + n[5]))**2)
    ca = math.sqrt((c1 + n[4] - (a1 + n[0]))**2 + (c2 + n[5] - (a2 + n[1]))**2)
    e = [ab,bc,ca] # salvam in lista pentru a le sorta
    e.sort()
    return e[0], e[1], e[2] # returnam ipotenuza , cateta1, cateta2

# verificam daca punctele introduse formeaza un triunghi drept
a3, b3, c3 = pitagora_th()
if is_triangle(c3, a3, b3):
    print('RIGHT')
    exit()
# verificam pentru conditia a doua 'ALMOST'
else:
    for i in range(6):
        moves ,movess = [0]*6, [0]*6 # 2 tabele de zerouri
        moves[i] = 1 # pe rand axtualizam al i-lea zerou in 1
        movess[i] =-1 # pentru tablelul 2 , i-lea punct il transformam in -1
        a, b, c = pitagora_th(moves) # verificam daca nu e dreptunghic inlocuind tabelul de zerouri cu cel de 1
        g, f, d = pitagora_th(movess)  # la fel verificam si pentru tabelul ce contine -1
        if is_triangle(c,b,a) or is_triangle(d,f,g): # afisam 'ALMOST' , daca cel putin o valoare returnata este True
            print('ALMOST')
            exit()
# in caz ca nu e satisfacuta nici o conditie
print('NEITHER')
