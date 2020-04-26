'''Problem 6A - Triangle'''
# citim lungimile, si le sortam in ordinea crescatoare
a,b,c,d=sorted(map(int,input().split()))

# verificam conditiile pentru ca segmentele sa fie triunghiuri
if a+b>c or b+c>d:
    print("TRIANGLE")
# daca nu este triunghi , verificam pt segment
elif a+b==c or b+c==d:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")
