'''Problem 11A - Increasing Sequence'''
n,d=map(int,input().split())
l1 = list(map(int, input().split())) # citim lista de numere
c =0
for i in range(1,len(l1)):
    if l1[i] <= l1[i-1]: # in caz ca 2 numere nus ordonate crescator
        # aplicam formula : nr de pasi = int((diferenta intre nr) / d+1)
        nr_ofSteps = (l1[i-1] - l1[i]) // d+1
        l1[i] += nr_ofSteps * d # actualizam elemntul l[i] ca sa corespunda conditie
        c += nr_ofSteps # actualizam nt toatal de pasi
print(c) # afisam nr total de pasi
