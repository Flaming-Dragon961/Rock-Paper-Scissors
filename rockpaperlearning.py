import random

print("Rock Paper Scissors, here is the game:")
x = input("What is your choice, rock, paper, or scissors?:") #opponent
y=["rock", "scissors", "paper"]
mm = random.randint(0, 2) #computer

def random_choice():
    try:
        if x=="rock" or "Rock":
            print(y[mm])
        elif x == "paper" or "Paper":
            print(y[mm])
        elif x == "scissors" or "Scissors":
            print(y[mm])
    except Exception as e:
        print("There is an error", e)

def computerrockwin():
    if mm==0 and x=="paper":
        print("Paper wins!")
    elif mm==0 and x=="scissors":
        print("Rock wins!")
    elif mm==0 and x=="rock":
        print("Tie!")

def computerscissorswin():
    if mm==1 and x=="paper":
        print("Scissors wins!")
    elif mm==1 and x=="scissors":
        print("Tie!")
    elif mm==1 and x=="rock":
        print("Rock wins!")

def computerpaperwin():
    if mm==2 and x=="paper":
        print("Tie!")
    elif mm==2 and x=="scissors":
        print("Scissors wins!")
    elif mm==2 and x=="rock":
        print("Paper wins!")


random_choice()
computerscissorswin()
computerrockwin()
computerpaperwin()


