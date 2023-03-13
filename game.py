# Setup
import random
answer = random.randint(1, 101)
user_wins = False
attempts = 0
attempt_word = ""

#Game loop
while user_wins != True:

        #Get user input
        guess =input("Enter a number between 1 and 100:")
        
        
        # Check the user input
        try:
            guess_number = int(guess)
        except:
            print("Error: Please a valid number is needed!")
            quit()
        #Increase attempt count
        attempts += 1
        
        #Check  the user answer against the secret number
        if guess_number == answer:
            user_wins = True
        elif guess_number > answer:
            print("The secret number is smaller!")
        else:
            print("The secret number is bigger!")
#Get the spelling of the "attempt" word
if attempts == 1:
    attempt_word = " attempt"
else:
    attempt_word =" attempts"

# Display the result or congratulation message
print("You won!!! You took " + str(attempts) + attempt_word)   
        