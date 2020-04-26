'''Problem 20A - BerOS file system'''
# citim datele si daca in sir este elementul '/' atunci il inlcuim cu ''
n = list(input().split('/'))
x =[]
# daca sirul e doar din 2 elemnte
# ['', 'litere'] sau ['/']
# afisam primul element '/' si caracterele ce urmeaza dupa el
if len(n)<=2:
    print('/', end='')
    for i in range(len(n)):
        if n[i] != '':
            print(n[i], end='')

else:
    # in caz ca lista n contine doar ''
    # afisam doar odata '/'
    if (len(set(n))==1):
        print('/')
    else:
        # adaugam elementele diferite de '' intr-o lista separata
        for i in n:
            if i != '':
                x.append(i)
        # afisam primul element ca '/'
        print('/', end='')
        for i in range(len(x)-1):
            # afisam elementele din lista cu caractere
            # la sfarsitul caracterelor afisam '/'
            print(x[i], end='/')
        # afisam ultimul element din lista cu caractere fara '/'
        print(x[-1])
