#importing 
import random

number = random.randint(1,10)

number_of_guesses = 0

number_of_chances =  5

while number_of_guesses < number_of_chances:
    
    print('Guess a number bettwen 1 and 10 !')
    guess = int(input('Guess: '))
    
    number_of_guesses = number_of_guesses + 1
    
    if guess < number:
        print("Your guess is too low." )
        
    if guess > number:
        print(f"Your guess is too high. You have " + number_of_chances " left")
        
    if guess == number:
        print('GOOD JOB YOU WON =-) !')
        
        break
    
if number_of_chances == 0:
    print('Aww you ran out of chances. The magic number was ' , number )
