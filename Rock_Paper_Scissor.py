import random
import time
def GameWinner(comp,user):
    if comp==user:
        return None
    elif comp=='Rock' or comp=='r' or comp=="ROCK" or comp=="R" or comp=="rock"  :
        if user=='Paper' or user=="paper" or user=="P" or user=="p" or user=="PAPER":
            return True
        elif user=='Scissor' or user=="S" or user=='s' or user=='scissor' or user=="SCISSOR":
            return False
    elif comp=='Paper' or comp=="paper" or comp=="P" or comp=="p" or comp=="PAPER":
        if user=='Scissor' or user=="S" or user=='s' or user=='scissor' or user=="SCISSOR":
            return True
        elif user=='Rock' or user=='r' or user=="R" or user=="rock" or user=="ROCK":
            return False
    elif comp=='Scissor' or comp=="s" or comp=="SCISSOR" or comp=="S" or comp=="scissor":
        if user=='Rock' or user=='r' or user=="rock" or user=="R" or user=="ROCK":
            return True
        elif user=='Paper' or user=='p' or user=='P' or user=='paper' or user=="PAPER":
            return False

print("Computer turn:Rock(r) Paper(p) Scissor(s)?")
num=random.randint(0,2)
if num==0:
    Input_Computer='Rock' or 'r' or 'rock' or 'R' or 'ROCK'
elif num==1:
    Input_Computer='Paper' or 'p' or 'paper' or 'P' or 'PAPER'
elif num==2:
    Input_Computer="Scissor" or 's' or 'scissor' or 'S' or 'SCISSOR'

print()
time.sleep(3)
print("Computer successfully choosed one option!")
print()
time.sleep(2)
MyTurn=input("Your Turn:Choose among r(Rock),p(Paper),s(Scissor):")
a=GameWinner(Input_Computer,MyTurn)

print()
print(f"Your choice:\n{MyTurn}")
time.sleep(2)
print(f"Computer choice:\n{Input_Computer}")

time.sleep(2)
print()
if a==None:
    print("Game is Tie.","\n","Better Luck next time!")
elif a:
    print("You win the game.","\n","Congratulations!")
else:
    print("You lost this game.","\n","Better Luck next time!")
