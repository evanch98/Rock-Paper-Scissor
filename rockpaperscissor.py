import random #To import random module

#Creating PC
class PC:
    def rps(self):
        self.rps_ = random.choice(['r', 'p', 's'])
        return self.rps_
    def getRPS(self):
        return self.rps_
computer = PC()

#Scores
player_score = 0
computer_score = 0

#Initialization
playGame = input("Hey Traveller, do you want to play rock, paper, scissor game? Type 'y' to play or 'n' to pass! ")
if playGame.lower() == 'y':
    play = True
elif playGame.lower() == 'n':
    play = False

#Game Logic
while play:    
    player1 = input("Type 'r' for Rock, 'p' for Paper or 's' for scissor: ")
    player1 = player1.lower()
    computer.rps()
    print("Player : {}, Computer : {}".format(player1, computer.getRPS()))
    if player1 not in ['r', 'p', 's']:
        print("Enter valid character!\n")
    elif player1 == 'r' and computer.getRPS() == 's':
        player_score += 1
    elif player1 == 'p' and computer.getRPS() == 'r':
        player_score += 1
    elif player1 == 's' and computer.getRPS() == 'p':
        player_score += 1
    elif player1 == 'r' and computer.getRPS() == 'p':
        computer_score += 1
    elif player1 == 'p' and computer.getRPS() == 's':
        computer_score += 1
    elif player1 == 's' and computer.getRPS() == 'r':
        computer_score += 1
    else:
        player_score += 0
        computer_score += 0
    print("Player 1 Score: {}, Computer Score : {}\n".format(player_score, computer_score))

    #Winning Condition
    if player_score == 15:
        replay = input("Congratulations, you win!!! Play again? Type 'y' for Yes or 'n' for No: ")
        if replay.lower() == 'y':
            player_score = 0
            computer_score = 0
        elif replay.lower() == 'n':
            play = False
    elif computer_score == 15:
        replay = input("Computer win, Try again? Type 'y' for Yes or 'n' for No: ")
        if replay.lower() == 'y':
            player_score = 0
            computer_score = 0
        elif replay.lower() == 'n':
            play = False
