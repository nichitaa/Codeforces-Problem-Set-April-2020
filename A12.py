'''Problem 12A - Super Agent'''
s = input()+input()+input()
# s = sirul care trebuie sal verificam daca e simetric
# s are 9 caractere (0 la 8)
# aplicam conditiile de simetrie
if s[:3]==s[8:5:-1] and s[0::3]==s[8::-3] :
    print('YES')
    exit()
print('NO')
