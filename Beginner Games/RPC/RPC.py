#RPC - Rock Paper Siccors will be a game played against the computer. The goal is to have a infinite loop that prompts the user to enter Rock, Paper or Siccors to initiate a new rount.
#The result will be compared against a randomized opponent. 
#Score will be kept and displayed after each round
#The program can be terminated by answering n to a prompted question to initiate a new round
import random
import time

score=[0,0]
tie=0
guess=""
rand_guess=""
wins=int(input("How many wins are needed for the game to end? - "))
while True:
    round_winner=[0,0]
    guess=input("Rock(r), Paper(p), Scissors(s)? - ")
    guess = guess.upper()
    time.sleep(0.5)
    #Check if the input is within the acceptable range
    accepted_strings=["ROCK", "PAPER", "SCISSORS", "R", "P", "S"]
    if guess not in accepted_strings:
        print("Please choose Rock(r), Paper(p) or Scissors(s):")
        continue


    #Translate all guesses to Rock/Paper/Scissors
    if guess == "R": guess="Rock"
    elif guess == "P": guess="Paper"
    elif guess == "S": guess="Scissors"
    print("You choose", guess)
    time.sleep(0.5)
    
    #Make the opponent guess randomly
    rand_guess_n = random.randint(0,2)
    
    #print(rand_guess_n)
    if rand_guess_n == 0:
        rand_guess="Rock"
        print("The opponent chooses Rock!")
    elif rand_guess_n == 1:
        rand_guess = "Paper"
        print("The opponent chooses Paper!")
    elif rand_guess_n == 2:
        rand_guess = "Scissors"
        print("The opponent chooses Scissors!")
    time.sleep(2)
    
    #Deduct who is the winner
    #Ties
    if guess == rand_guess:
        print("Tie! The score remains unchanged")

    #Losses
    if guess =="Rock" and rand_guess=="Paper":
        print("You loose to Paper!")
        round_winner[1]=1
    if guess =="Paper" and rand_guess=="Scissors":
        print("You loose to Scissors!")
        round_winner[1]=1
    if guess =="Scissors" and rand_guess=="Rock":
        print("You loose to Rock!")
        round_winner[1]=1

    #Wins
    if guess =="Rock" and rand_guess=="Scissors":
        print("You win vs Scissors!")
        round_winner[0]=1
    if guess =="Paper" and rand_guess=="Rock":
        print("You win vs Rock!")
        round_winner[0]=1
    if guess =="Scissors" and rand_guess=="Paper":
        print("You win vs Paper!")
        round_winner[0]=1

    if round_winner == [0,0]:
        tie += 1
    time.sleep(1)
    score[0] = score[0] + round_winner[0]
    score[1] = score[1] + round_winner[1]
    print("The score is ", score[0]-score[1])
    time.sleep(1)
    print("Your wins:", score[0], "\nOpponent wins:", score[1], "\nTies: ", tie)
    
    #Exit prompt
    
    if score[0] == wins:
        #Print the score and exit message
        print("You won!! The final score is ", score[0], "-", score[1])
        print("Your win percentage was: ", (score[0]/(score[1]+tie+score[0]))*100, "%")
        if input("Play another round? (y/n)\n") == "n":
            break
        else: 
            wins=int(input("How many wins are needed for the game to end? - "))
            score=[0,0]
            tie=0
    if score[1] == wins:
        #Print the score and exit message
        print("Game over! The final score is ", score[0], "-", score[1])
        print("Your win percentage was: ", (score[0]/(score[1]+tie+score[0]))*100, "%")
        if input("Play another round? (y/n)\n") == "n":
            break
        else: 
            wins=int(input("How many wins are needed for the game to end? - "))
            score=[0,0]
            tie=0