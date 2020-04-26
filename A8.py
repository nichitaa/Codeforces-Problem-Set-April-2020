'''Problem 8A - Train and Peter'''
colors = (input()) # stringul de culori
f = (input()) # prima faza
s = (input()) # a doua faza
forw = 0
# verific daca e culorile din prima si a doua faza sunt in colors
# in ordinea lor normala
if f in colors: # daca prima faza este in colors
    f_idx = colors.index(f)
    _f = f_idx+len(f) # salvam ultimul index
    if s in colors[_f:]: # verificam incepand cu ultimul index pentru a doua faza
        forw = 1
way_back = colors[::-1] # way back = stringul inversat
back = 0
# repetam aceiasi procedura si pentru drumul invers
if f in way_back:
    f_idx = way_back.index(f)
    _f = f_idx+len(f)
    if s in way_back[_f:]:
        back = 1
# afisam raspunsurile
if forw == 1 and back == 1 :   print('both')

elif forw == 1 and back == 0 : print('forward')

elif forw == 0 and back == 1 : print('backward')

elif forw == 0 and back == 0 : print('fantasy')
