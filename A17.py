'''Problem 17A - Noldbach problem'''
n,k=map(int,input().split()) # citim n si k
primes = []
# toate numerele prime pana la n+1 le salvam in lista primes
for num in range(2,n+1):
    if all(num % i != 0 for i in range(2,num)):
        primes.append(num)
c=0
# verificam conditia
for i in range(len(primes)-1):
	# daca suma a doua numere vecine si adunate cu 1 este un nr prim din lista primes
	# incrementam c
	if primes[i]+primes[i+1]+1 in primes:
		c+=1

# afisam rezultatul
if(c>=k):
	print("YES")
else:
	print("NO")
