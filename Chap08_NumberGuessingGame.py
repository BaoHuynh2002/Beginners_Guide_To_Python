# Number Guessing Game
# - The program randomly selects a number between 1 and 10.
# - It will then ask the player to enter their guess.
# - It will then check to see if that number is the same as the one the computer
# randomly generated; if it is then the player has won.
# - If the player’s guess is not the same, then it will check to see if the number is
# higher or lower than the guess and tell the player.
# - The player will have 4 goes to guess the number correctly; if they don’t guess
# the number within this number of attempts, then they will be informed that they
# have lost the game and will be told what the actual number was.
# - Provide a cheat mode, for example if the user enters −1 print out the number
# they need to guess and then loop again. This does not count as one of their goes.
# - At the end of the game, before printing 'Game Over', modify your program so
# that it asks the user if they want to play again; if they say yes then restart the
# whole thing.
import random
print('NUMBER GUESS GAME')
play_again = True
while play_again:
    num_to_guess = random.randint(1,10)
    time_of_guess = 1
    guess = input('# Please guess a number in range (1,10): ')
    while guess.isnumeric() == bool(0) or int(guess) > 10 or int(guess) <1:
        guess = input('# Please guess a number in range (1,10): ')
    guess = int(guess)
    while num_to_guess != guess:
        print('@ Sorry its wrong')
        if time_of_guess == 4:
            break
        elif guess < num_to_guess:
            print('@ Your guess was lower than the number')
        else:
            print('@ Your guess was higher than the number')
        print('-'*10)
        # Obtain their next guess and increment number of attempts
        guess = int(input('# Please guess again: '))
        time_of_guess += 1
    if num_to_guess == guess:
        print('-'*10)
        print('Well done you won!')
        print('You took', time_of_guess, 'goes to complete the game')
    else:
        print('-' * 10)
        print("Sorry - you loose")
        print('The number you needed to guess was', num_to_guess)
        print('Game Over')
    play_again = bool(int(input('> Play again ? (0: No, 1: Yes): ')))
print('~Bye~')