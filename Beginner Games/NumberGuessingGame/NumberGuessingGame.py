#This program will have the user guess a number. Give hints to the correct answer (higher/lower) and track how many guesses the user needs to find the number.
import random
import time
import shelve

d = shelve.open('score.txt')
high_score = d['score']
if 'name' in d:
    hs_name = d['name']
else: 
    d['name'] = ""
    hs_name = ""
d.close()
score = 0
user_name = input("Hello! What is your name? - ")
print("Ok " + user_name + ", we are going to play a guessing game.")
print("You will choose a range of numbers and I will choose a number within that range at random.")
print("Then you get to guess the number and I will give you hints after each guess.")
print("Once you are correct i will present your score.\n")
time.sleep(1)
number_range=int(input(user_name + " in what range do you want me to select a number? (0 - ?) - "))
while True:
    input("Current High Score is " + str(format(high_score,".2f")) + " by " + hs_name + "\n\nPress Enter to continue\n")
    while number_range < 1:
        number_range = int(input("Please select a positive number! - "))
    target = random.randint(0,number_range)
    guess = -1
    n_guess = 0

    print("Guess the number!")
    while guess != target:
        guess=int(input("Guess number " + str(n_guess + 1) + " : "))
        if guess > number_range:
            print("You guessed outside the range! Please try again (0 - " + str(number_range) + ")" )
        n_guess += 1
        if guess < target:
            print("Your guess was too low, try again")
        elif guess > target:
            print("Your guess was too high, try again")            
        elif guess == target:
            print("Correct! The number was " + str(target))
            time.sleep(1)
            score= number_range / (20 * n_guess)
            print("Your score is " + str(format(score,".2f")))
            if high_score < score:
                print("-------------------------------------------------\nThat is a new High Score!! Congratulations\n-------------------------------------------------")
                high_score = score
                d= shelve.open('score.txt')
                d['score'] = high_score
                d['name'] = user_name
                hs_name = d['name']
                d.close()
    prompt = input("Do you want to play again? Select the new range (n to exit)")
    if prompt == "n":
        break
    else:
        number_range = int(prompt)



