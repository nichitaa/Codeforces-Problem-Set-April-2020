'''Problem 2A - Winner'''
n = int(input()) # nr de ture
game = []
scores = {}

for i in range(n):
    player,score = (input().split()) # citim jucatorul si scorul lui
    scores[player] = scores.get(player,0) + int(score) # adaugam jucatourul in dictionar si de fiecare data ii actualizam scorul
    game.append([player, scores[player]]) # adaugam tura curenta in lista games (cu scorul jucatorului deja actualizat) pentru a putea reproduce jocul
max_score = max(scores.values()) # determinam care este valoarea maxima de puncte acumulate
# simulam joaca inca odata
print(game)
for i, j in game:
    # daca in tura i jucatorul a strans max de puncte, atunci el a biruit
    if scores[i] == max_score and int(j)>=max_score:
        print(i)
        break
