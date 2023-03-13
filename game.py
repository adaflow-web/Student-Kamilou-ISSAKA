# Setup
import random
answer = random.randint(1, 101)
user_wins = False
attempts = 0

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
        
        #Check  the user answer against the secret number
        
#Get the spelling of the "attempt" word 

# Display the result or congratulation message   
        