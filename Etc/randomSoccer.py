import random
import sys

simPersonNum=3
teamNum=9

player_name=[]
team=[[None for i in range(9)] for j in range(3)]
print("비슷한 실력의 선수들을 3명 씩 적어주십쇼")
for i in range(teamNum):
    similarPerson = list(map(str,sys.stdin.readline().split()))
    player_name.append(similarPerson)
for i in range(teamNum):
    random.shuffle(player_name[i])
    for j in range(simPersonNum):
        team[j][i] = player_name[i][j]
for i in range(simPersonNum):
    print("-------------------------------------")    
    print(f"{i} 팀 : {team[i]}")
print("-------------------------------------")
