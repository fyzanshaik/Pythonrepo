from random import randint

print("...rock...\n...paper...\n...scissor...")
player = input("Enter player choice : ")

rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissor"

print(f"Computer plays {computer} ")

if player == computer:
    print("STALEMATE!")
elif player == "rock":
    if computer == "paper":
        print("SHOOT!")
        print("computer WINS!")
    elif  computer == "scissor":
        print("SHOOT!")
        print("player WINS!")
elif player == "paper":
    if computer == "rock":
        print("SHOOT!")
        print("player WINS!")
    elif  computer == "scissor":
        print("SHOOT!")
        print("computer WINS!")
elif player == "scissor":
    if computer == "paper":
        print("SHOOT!")
        print("player WINS!")
    elif computer == "rock":
        print("SHOOT!")
        print("computer WINS!")
else:
    print("Incorrect Input, run again!")