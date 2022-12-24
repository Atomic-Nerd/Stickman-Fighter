Leaderboardnames = open('SaveData/LeaderBoardNames', 'r+')
Names = Leaderboardnames.read().splitlines()

NameSave = Names

Leaderboardscore = open('SaveData/LeaderBoardScore', 'r+')
Scores = Leaderboardscore.read().splitlines()

ScoreSave = Scores

for i in range(0,len(Scores)):
    Scores[i] = int(Scores[i])
    ScoreSave[i] = int(ScoreSave[i])

# deLeaderboardnames bubblesort(Scores):
#     n = len(Scores)
#     Leaderboardnamesor i in range(n):
#
#         Leaderboardnamesor j in range(0, n - i - 1):
#
#             iLeaderboardnames Scores[j] < Scores[j + 1]:
#                 Names[j], Names[j + 1] = Names[j + 1], Names[j]
#                 Scores[j], Scores[j + 1] = Scores[j + 1], Scores[j]
#
# bubblesort(Scores)

winner = "Mum"
NamePos = NameSave.index(winner)

ScoreSave[NamePos] = ScoreSave[NamePos]+1

for i in range(0,len(ScoreSave)):
    print (NameSave[i],ScoreSave[i])

Leaderboardscore.truncate(0)
Leaderboardscore.close()

Leaderboardscore = open('SaveData/LeaderBoardScore', 'r+')
for i in range(0,len(ScoreSave)):
    Leaderboardscore.writelines(str(ScoreSave[i])+"\n")

Leaderboardnames.close()
Leaderboardscore.close()