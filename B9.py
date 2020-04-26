'''Problem 9B - Running Student'''

import math
# functie pentru calculul distantei
def dist(x1, y1, x2, y2):
    return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )
n, vb, vs = map(int,input().split()) # citim nr. de statii, viteza autobuzului, viteza studentului
stations = list(map(int,input().split())) # citim coordinatele statiilor
xu, yu = map(int,input().split()) # citim coordinatele universitatii

minStation, Shortest_time = None, None

for i in range(len(stations)):
    if i == 0: continue
    # timpul de la statia curenta pana la universitate , luand in considerare viteza autobuzului si viteza studentului
    # t = drumul parcurs de autobus / viteza autobuzului + distanta intre statia curenta si universitate / viteza studentului
    Shortest_time = stations[i]/vb + dist(stations[i], 0, xu, yu)/vs
    # pentru prima iteratie este conditie:  if minStation == None
    # pentru urmatoarele iteratii verificam daca timpul curent este mai mic ca timul minim deja salvat
    # sau daca timpul curent este egal cu timpul minim si distanta dintre statia curenta si universitate este mai mica ca distanta dintre stantia deja salvata si universitate
    if minStation == None or Shortest_time < minVal or (Shortest_time == minVal and dist(stations[minStation], 0, xu, yu) > dist(stations[i],0,xu,yu)):
        minStation = i
        minVal = Shortest_time
# afisam nr la statie
print( minStation + 1)
