'''Problem 5C - Longest Regular Bracket Sequence'''

stack = [-1] # initializam o lista cu primul element -1, care va fi stackul gol
res = 0
nr_OfSubsequences = 1 # incaz ca nu au fosta gasite mai multe subsiruri trebuie sa afisam (0 1)
signs = input() # citim sirul

# iteram prim sir
for i in range(len(signs)):
    if signs[i] == '(': # daca elemntul i al sirului este simbolul '('
        stack.append(i) # adaugam indexul i in stack
    # daca element i al sirului este ')' si lungimea stacul coontine mai mult de 1 element adica nu e gol ([-1])
    elif len(stack) > 1:
        stack.pop() # eliminam ultimul element din stack , precum au fost gasite un semn de deschider a parantezelor si de inchidere
        top = stack[-1] # top este ultimul element al stackului dupa actualizarea stackului de mai sus
        curr_lenght = i - top # lungime curenta a subsiruli valid de '()' este , indexul element sirului - indexului ultimului element al stackului
        # daca lungimea curenta a subsirului curent este mai mare ca lungimea subsirului deja salvat
        if curr_lenght > res:
            res = curr_lenght # actualizam res = lungime_celui_mai_lung_subsir_valid
            nr_OfSubsequences = 1
        # in caz ca a fost gasit inca un sir de aceiasi lungime
        elif res == curr_lenght:
            nr_OfSubsequences += 1 # actualizam nr de subsiruri
    # deca stackul e gol ([-1])
    else :
        stack[0] = i # adaugam indexul i in stack
print('%d %d' %(res, nr_OfSubsequences)) # afisam lungimea celui mai lung subsir si nr total de subsiruri valide
