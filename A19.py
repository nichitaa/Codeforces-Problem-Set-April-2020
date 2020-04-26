'''Problem 19A - World Football Cup'''
score = {} # dict pentru a face totalurile pentru fiecare din jucatori
n = int(input()) # citim nr de echipe
for i in range(n):
    team = input() # key = numele la echipe
    score[team] = [0,0,0] # numele la echipa = [puncte pentru fiecare match,
                                            # diferenta intre golurile marcate si primite,
                                            # toate golurile marcate ]
# citim rezultatele meciurilor
for _ in range(n*(n-1)//2):
    data = input().split()
    teams = data[0].split('-') # teams = ['team_first', 'team_second']

    first_team = teams[0] # first team
    sec_team = teams[1] # second team

    scores = data[1].split(':')
    first_tscore = int(scores[0]) # score for first_team
    sec_tscore = int(scores[1]) # score for sec_team

    # in caz ca a doua echipa a chastigat
    if first_tscore < sec_tscore:
        score[sec_team][0] += 3 # 'sec_team_name' = [3,0,0]
        score[sec_team][1] += sec_tscore - first_tscore # 'sec_team_name' = [3,diferenta intre goluri,0]
        score[sec_team][2] += sec_tscore # 'sec_team_name' = [3,diferenta intre goluri,goluri marcate in meci]
        # la fel si pentru echipa 1 actualizam scorurile in dictionarul score
        score[first_team][1] += first_tscore - sec_tscore
        score[first_team][2] += first_tscore

    # in caz ca echipa 1 a biruit
    if first_tscore > sec_tscore:
        score[first_team][0] += 3
        score[first_team][1] += first_tscore - sec_tscore
        score[first_team][2] += first_tscore

        score[sec_team][1] += sec_tscore - first_tscore
        score[sec_team][2] += sec_tscore

    # in caz de egalitate
    elif first_tscore == sec_tscore:
        score[first_team][0] += 1
        score[first_team][1] += first_tscore - sec_tscore
        score[first_team][2] += first_tscore

        score[sec_team][0] += 1
        score[sec_team][1] += sec_tscore - first_tscore
        score[sec_team][2] += sec_tscore

# print(score)
res = [] # valorile din dictionar le salvam in lista res
# team = key , # score = list of scores for each team
for team, score in score.items():
    res.append([score[0], score[1], score[2], team]) # : res = [[5, 1, 4, 'A'], [4, -2, 2, 'B'], [1, -4, 2, 'C'], [6, 5, 6, 'D']]

res = sorted(res) # sortam lista , dupa condtitie
res.reverse() # reversam lista , ca echipele cu cele mai mari scoruri sa fie primele

nw = [] # lista pt echipele care sau calificat
for i in range(n//2):
    nw.append(res[i][3]) # adougam in lisa numele acestor echipe

nw = sorted(nw)
print(*nw, sep='\n') # afisam numele la echipe din rand nou
