str1='''It is the match between <TEAM1> and <TEAM2>'''
Team1=int(input("score of team1:"))
Team2=int(input("score of team2:"))
Team3=int(input("score of team3:"))
Team4=int(input("score of team4:"))

if Team1==Team2:
    print("Super over")
elif Team1>Team2:
    Finalist1=Team1
else:
    Finalist1=Team2

if Team3==Team4:
    print("Super over")
elif Team3>Team4:
    Finalist2=Team3
else:
    Finalist2=Team4

if Finalist1>Finalist2:
    print("Winner is Finalist1 with score",Finalist1)
else:
    print("Winner is Finalist2 with score",Finalist2)



