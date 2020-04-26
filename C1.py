'''Problem 1C - Ancient Berland Circus'''

import math
# returnam lungimile laturilor (l1,l2,l3)
# folosim formula lui pitagora
# l1 = sqrt( ((x2 - x1)**2) + ((y2 - y1)**2) )
# l2 = sqrt( ((x3 - x2)**2) + ((y3 - y2)**2) )
# l3 = sqrt( ((x3 - x1)**2) + ((y3 - y1)**2) )
def ToEdgePt(p):
    l1 = (((p[1][0] - p[0][0])**2) + ((p[1][1] - p[0][1])**2))**(1/2)
    l2 = (((p[2][0] - p[1][0])**2) + ((p[2][1] - p[1][1])**2))**(1/2)
    l3 = (((p[2][0] - p[0][0])**2) + ((p[2][1] - p[0][1])**2))**(1/2)
    return [l1,l2,l3]

# returnam masurile unghiurilor dintre laturi
# a1 = acos((l2**2 + l3**2 - l1**2) / (2*l2*l3)))
# a2 = acos((l1**2 + l3**2 - l2**2) / (2*l1*l3)))
# a3 = acos((l1**2 + l2**2 - l3**2) / (2*l1*l2)))
def angles(e):
    a1 = math.acos( (e[1]**2 + e[2]**2 - e[0]**2 ) / (2*e[1]*e[2]) )
    a2 = math.acos( (e[0]**2 + e[2]**2 - e[1]**2 ) / (2*e[0]*e[2]) )
    a3 = math.acos( (e[0]**2 + e[1]**2 - e[2]**2 ) / (2*e[0]*e[1]) )
    return [a1,a2,a3]

# returnam aria triunghiului
# A = (1/2) * (l2*l3*sin(l3))
def Area(e, a):
    return (e[0] * e[1] * math.sin(a[2])) / 2

# raza cercului circumscris = ( l1 * l2 * l3 ) / ( 4 * area )
def Raza(e, area):
    return ( (e[0] * e[1] * e[2]) / (4 * area) )

# returnam numarul minim de piloni posibil
# nr = math.pi / (math.gcd( math.gcd(a1, a2) ), a3)
# unde a - masurile unghiurilor
def MinPiloni(a):
    return math.pi / ( float_gcd( float_gcd(a[0], a[1]), a[2] ))

# raspunsul :
# aria circului = nr / 2 * raza**2 * math.sin(2*math.pi / nr)
def FinalArea(nr, raza):
    return (nr / 2 * raza**2 * math.sin(2*math.pi / nr))

# derminam gcd recursiv pentru numerele float , cu toleranta de 0.001
def float_gcd(a,b) :
    if (a < b) :
        return float_gcd(b, a)
    if (abs(b) < 0.001) :
        return a
    else :
        return (float_gcd(b, a - math.floor(a / b) * b))

points = [] # lista pentru punctele initiale
for i in range(3):
    points.append(list(map(float, input().split()))) # inputul

e = ToEdgePt(points) # determinam lungimile laturilor
a = angles(e)  # determinam masurile unghiurilor
A = Area(e,a) # determinam area triunghiuui
R = Raza(e, A) # determinam raza cercului circumscris triunghiului
piloni = MinPiloni(a) # determinam nr de piloni
print('%.8f' %(FinalArea(piloni, R))) # afisam raspunsul cu 8 cifre dupa virgula
