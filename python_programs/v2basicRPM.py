print("...rock...\n...paper...\n...scissor...")

player1 = input("Enter player1's choice : ")

print("***NO CHEATING***\n\n***NO CHEATING***" * 30 )

player2 = input("Enter player2's choice : ")

if player1 == player2:
    print("STALEMATE!")
elif player1 == "rock":
    if player2 == "paper":
        print("SHOOT!")
        print("player2 WINS!")
    elif  player2 == "scissor":
        print("SHOOT!")
        print("player2 WINS!")
elif player1 == "paper":
    if player2 == "rock":
        print("SHOOT!")
        print("player1 WINS!")
    elif  player2 == "scissor":
        print("SHOOT!")
        print("player2 WINS!")
elif player1 == "scissor":
    if player2 == "paper":
        print("SHOOT!")
        print("player1 WINS!")
    elif player2 == "rock":
        print("SHOOT!")
        print("player2 WINS!")
else:
    print("Incorrect Input, run again!")