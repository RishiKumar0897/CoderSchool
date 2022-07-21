import random
import time
import os

maxNum = 100
minNum = 1
#generate random number
target_number = random.randint(minNum,maxNum)
num_of_guesses = 10
time_limit = 15
elapsed = 0 
guessed_numbers = []
print("Welcome to Guess the Number!")
print("Guess the number between " + str(minNum) + " and " + str(maxNum) + " in " + str(time_limit) + " seconds")
guess = 0

#game loop
while num_of_guesses > 0 and guess!= target_number:

    start = time.time() #current time
    end_time = start + time_limit
    print("Lives left: " + str(num_of_guesses))
    print("Guessed Numbers: " + str(guessed_numbers))
    print("You have " + str(time_limit) + " seconds to answer")
    guess = int(input("Your guess: "))

    if guess > target_number:
        print("Too high!")
        num_of_guesses -= 1
        guessed_numbers.append(guess)
        if num_of_guesses == 0:
            print("No more lives, try again next time!")
            print("The number was " + target_number)
            break
        if time.time() > end_time:
            print("Sorry, you ran out of time!")
            print("The number was " + target_number)
            break
        time.sleep(1)
        os.system("clear")
        
    elif guess < target_number:
        print("Too low!")
        num_of_guesses -=1
        guessed_numbers.append(guess)
        if num_of_guesses == 0:
            print("No more lives, try again next time!")
            print("The number was " + target_number)
            break
        if time.time() > end_time:
            print("Sorry, you ran out of time!")
            print("The number was " + target_number)
            break
        time.sleep(1)
        os.system("clear")
        
    else:
        print("You got it with " + str(num_of_guesses) + " lives left!" + "The number was: " + str(guess))
        guessed_numbers.append(guess)
        time.sleep(5)
        
    
        

