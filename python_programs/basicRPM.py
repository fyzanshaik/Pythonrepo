print("...rock...\n...paper...\n...scissor...")

chance1 = input("Enter player1's choice : ")

print("***NO CHEATING***\n***NO CHEATING***" * 30 )

chance2 = input("Enter player2's choice : ")

if chance1 == "rock" and chance2 == "paper":
    print("SHOOT!")
    print("player2 WINS!")
elif chance1 == "rock" and chance2 == "scissor":
    print("SHOOT!")
    print("player1 WINS!")
elif chance1 == "paper" and chance2 == "rock":
    print("SHOOT!")
    print("player1 WINS!")
elif chance1 == "paper" and chance2 == "scissor":
    print("SHOOT!")
    print("player2 WINS!")
elif chance1 == "scissor" and chance2 == "paper":
    print("SHOOT!")
    print("player1 WINS!")
elif chance1 == "scissor" and chance2 == "rock":
    print("SHOOT!")
    print("player2 WINS!")
elif chance1 == chance2:
    print("STALEMATE!")

else:
    print("Incorrect Input, run again!")