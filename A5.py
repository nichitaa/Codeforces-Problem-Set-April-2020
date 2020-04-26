'''Problem 5A - Chat Servers Outgoing Traffic'''

from sys import *
live = 0
l = 0
for line in stdin: # pentru linie in input
    # daca persoana a intrat in chat
    # actualizam nr de persoane
    if line[0] == "+":
        live += 1
    # daca o persoana a iesit
    # actualizam nr de persoane
    elif line[0] == "-":
        live -= 1
    # daca cineva a trimis un mesaj
    # inmultim lungimea mesajului la nr de persona ce sunt la moment in chat
    else :
        idx = line.find(':')
        line = line[idx+1:]
        l = l + (len(line)-1)*live
# afisam raspunsul
print(l)
