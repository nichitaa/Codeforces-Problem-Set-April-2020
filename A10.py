'''Problem 10A - Power Consumption Calculation'''

# citim nr de intervale de lucru, power plan 1 pana la 3
# si intervalurile de timp pentru schimbarea power planurilor
n,P1,P2,P3,T1,T2 = map(int,input().strip().split())
active = [] # lista pentru intervalul in care se foloseste power plan 1
res = 0 # res = resultatul final (cata energie a fost consumata)
for i in range(n):
	active.append(list(map(int,input().strip().split()))) # citim intervalurile de
	 											# timp in care sa lucrat la laptop

# in caz ca avem doar un interval de timp activ
# afisam imediat raspunsul
if len(active) == 1 :
	print((active[0][1]-active[0][0])*P1)
# cand avem mai multe intervale active
else:
	for i in range(len(active)):
		# daca am ajuns la ultimul interval activ de timp afisam raspunsul
		if i == len(active)-1 :
			res += (active[i][1] - active[i][0]) * P1
			print(res)
			exit()
		# in res salvam energia totala consumata de pc
		# actualizam res cu energia consumate de power plan 1
		res += (active[i][1] - active[i][0]) * P1
		# idle = intervalul de timp intre intervalele active
		idle = active[i+1][0] - active[i][1]
		# daca exista timp de idle dar e mai mic ca timpul necesar pt power plan 2
		if idle <= T1 and idle > 0:
			res += idle*P1 # actualizam res cu power plan 1 si timpul de idle ramas
		# daca e suficient timp pentru ca pc sa treaca in power plan 2 :
		if idle > T1:
			res += T1*P1 # actualizam res cu Timpul necesar trecerii in power plan 2 si T1
			idle -= T1 # actualizam timpul ramas pt idle
			# daca timpul de idle ramas nu e suficient pt a trece in power plan 3
			if idle > 0 and idle <= T2:
				res += idle*P2 # actualizam res, timpul rams * power plan 2
			# daca e suficient timp pentru a trece din idle in sleep mode cu power plan 3
			elif idle > T2:
				# actualizam res cu timpul necesar pt efectuarea trecerii in power plan 3
				res += T2*P2
				idle -= T2 # actualizam timpul ramas pt power plan 3
				if idle > 0:
					res += idle*P3 # actualizam res cu timpul petrecut in power plan 3
