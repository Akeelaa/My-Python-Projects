
# Im creating a number guessing game 
# python will pick random number between 1 - 100
# and the user will try and guess it
# each time they guess it incorectly you code will say 
# you need guess higher or lower next time.
# eventually when the user gets the right asnwer it will
# say you got the right asnwer which was 42 and it took you 7 tries.

import random 
import time 


print(" Welcome! to the guessing game im going to pick a number from 1 too 100")
time.sleep(3) # adding a 3 second pause to add some suspense to the game
print("picking a number... Get ready to guess some numbers :)")
time.sleep(2)
user_guess = int(input("What is your guess? :"))

guess_count = 1
correct_number = random.randint(1,100)

while user_guess != correct_number:
    time.sleep(1)
    guess_count += 1
    if user_guess < correct_number:
        user_guess = int(input("Wrong! You need to guess higher. What is you guess?:"))
        
    else:
        
        user_guess = int(input("Wrong! You need to guess lower. What is you guess?:"))

print(f"""
Hey Congrats!! 
You got the right answer which was: {correct_number}. 
It took you: {guess_count} guesses.
""")

