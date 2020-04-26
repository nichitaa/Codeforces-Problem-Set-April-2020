'''Problem 4C - Registration System'''

n = int(input()) # citim numarul de inregistrari in sistem
reg = []
reg_dict = dict() # dictionar pentru a salva nr de aparatii a unui nume in lista reg
                  # dupa modelul
                  # reg_dict[ 'nume_unic' ] : nr_de_aparitii_in_lista
                  # reg_dict[ key ] : <integer_value>
for i in range(n):
    s = str(input()) # fiecare nume il salvalm lista reg
    reg.append(s)

for s in reg : # iteream in lista reg
    if s not in reg_dict: # daca numele s nu este in dictionar , afisam 'ok'
        print('OK')
        reg_dict[s] = 1 # si il adaugam in dictionar cu valoarea 1, precum a fost
                        # deja intalnit odata
    # daca numele este in dictionar deja
    else :
        print(s+str(reg_dict[s])) # afisam numele + valaoarea atribuita lui, adica
                                  # numarul de aparatii a acestui nume in iteratiile anterioare
        reg_dict[s] += 1 # actualizam valoarea numelui (nr de aparitii anterioare)
