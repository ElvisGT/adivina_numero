
import random

logo = """
  /$$$$$$$$/$$                      /$$   /$$                      /$$                                /$$$$$$                                    /$$                          /$$$$$$                                
 |__  $$__| $$                     | $$$ | $$                     | $$                               /$$__  $$                                  |__/                         /$$__  $$                               
    | $$  | $$$$$$$  /$$$$$$       | $$$$| $$/$$   /$$/$$$$$$/$$$$| $$$$$$$  /$$$$$$  /$$$$$$       | $$  \__//$$   /$$ /$$$$$$  /$$$$$$$/$$$$$$$/$$/$$$$$$$  /$$$$$$       | $$  \__/ /$$$$$$ /$$$$$$/$$$$  /$$$$$$ 
    | $$  | $$__  $$/$$__  $$      | $$ $$ $| $$  | $| $$_  $$_  $| $$__  $$/$$__  $$/$$__  $$      | $$ /$$$| $$  | $$/$$__  $$/$$_____/$$_____| $| $$__  $$/$$__  $$      | $$ /$$$$|____  $| $$_  $$_  $$/$$__  $$
    | $$  | $$  \ $| $$$$$$$$      | $$  $$$| $$  | $| $$ \ $$ \ $| $$  \ $| $$$$$$$| $$  \__/      | $$|_  $| $$  | $| $$$$$$$|  $$$$$|  $$$$$$| $| $$  \ $| $$  \ $$      | $$|_  $$ /$$$$$$| $$ \ $$ \ $| $$$$$$$$
    | $$  | $$  | $| $$_____/      | $$\  $$| $$  | $| $$ | $$ | $| $$  | $| $$_____| $$            | $$  \ $| $$  | $| $$_____/\____  $\____  $| $| $$  | $| $$  | $$      | $$  \ $$/$$__  $| $$ | $$ | $| $$_____/
    | $$  | $$  | $|  $$$$$$$      | $$ \  $|  $$$$$$| $$ | $$ | $| $$$$$$$|  $$$$$$| $$            |  $$$$$$|  $$$$$$|  $$$$$$$/$$$$$$$/$$$$$$$| $| $$  | $|  $$$$$$$      |  $$$$$$|  $$$$$$| $$ | $$ | $|  $$$$$$$
    |__/  |__/  |__/\_______/      |__/  \__/\______/|__/ |__/ |__|_______/ \_______|__/             \______/ \______/ \_______|_______|_______/|__|__/  |__/\____  $$       \______/ \_______|__/ |__/ |__/\_______/
                                                                                                                                                             /$$  \ $$                                               
                                                                                                                                                            |  $$$$$$/                                               
                                                                                                                                                             \______/                                              
"""


def find_number(random_number, attempts):
    i = attempts
    while i > 0:
        print(f"You have {i} attempts remaining to guess the number.")
        user_number = int(input("Make a guess: "))

        if user_number == random_number:
            print(f"You got it! The answer was {user_number}.")
            break

        if user_number > random_number:
            print("Too high.")
            print("Guess again.")
            
        
        if user_number < random_number:
            print("Too low.")
            print("Guess again.")
            
        
        i -= 1
    
    print("You've run out of guesses, you lose.")
    exit(0)
  
def main():
    attempts = 0
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100)
    print(f"Pssst, the correct answer is {random_number}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    #Determinando dificultad
    if difficulty.lower() == 'easy':
        attempts = 10
    else:
        attempts = 5

    #Logica de juego
    find_number(random_number, attempts)


#Ejecucion
main()
