'''Problem 9A - Die Roll'''
x = list(map(int,input().split()))
m = max(x) # nr maxim care deja a fost aruncat la zare
# toate probabilitatile posibile (deja simplificate)
prob = ['1/1','5/6','2/3','1/2','1/3','1/6']
# afisam probabilitatile ce ne corespunde
print(prob[m-1])
