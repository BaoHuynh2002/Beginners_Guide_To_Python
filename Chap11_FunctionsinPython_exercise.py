# Remake the Number Guessing Game (Chap8) using Functions (Chap11)
import random


# Function: take input from player
def player_input(msg):
    guess = input(msg)
    while guess.isnumeric() == bool(0) or int(guess) > 10 or int(guess) < 1:
        guess = input(msg)
    guess = int(guess)
    return guess


# Function: show message when player win
def msg_win(time_of_guess):
    print('-' * 10)
    print('Well done you won!')
    print('You took', time_of_guess, 'goes to complete the game')


# Function: show message when player lose
def msg_lose(num_to_guess):
    print('-' * 10)
    print("Sorry - you loose")
    print('The number you needed to guess was', num_to_guess)
    print('Game Over')


# Function: show suggestion after player guess
def suggestion(x):
    if x:
        print('@ Your guess was lower than the number')
    else:
        print('@ Your guess was higher than the number')
    print('-' * 10)


# Function: Game Function has 4 functions above
def game():
    num_to_guess = random.randint(1, 10)
    time_of_guess = 1
    guess = player_input('# Please guess a number in range (1,10): ')
    while num_to_guess != guess:
        print('@ Sorry its wrong')
        if time_of_guess == 4:
            break
        else:
            suggestion(guess < num_to_guess)
        # Obtain their next guess and increment number of attempts
        guess = player_input('# Please guess again: ')
        time_of_guess += 1
    if num_to_guess == guess:
        msg_win(time_of_guess)
    else:
        msg_lose(num_to_guess)


# Function: let user play again or not , main function has game function above
def main():
    print('NUMBER GUESS GAME')
    play_again = True
    while play_again:
        game()
        play_again = bool(int(input('> Play again ? (0: No, 1: Yes): ')))
    print('~Bye~')


# call main() Function
main()
