'''Problem 1A - Theatre Square'''

n,m,a=map(int,input().split())
# in caz ca latimea placa are mairime de 1x1
# afisam coloanele * randuri
if a==1:
    print(n*m)
# in caz ca placa ocupa toata suprafata
elif n==m and m==a : print(1)

else:
    # determinam cate placi sunt necesare
    # pt un rand
    if m%a==0:
        r=m//a
    # in caz ca nu e divizor , adaugam cu surplus
    else:
        r=m//a+1
    # pt o coloana
    if n%a==0:
        c=n//a
    else:
        c=n//a+1
    # afisam raspunsul 
    print(r*c)
