import random
import time


def print_pause(message, sleep_time=0.5):
    print(message)
    time.sleep(sleep_time)


def guess_intro(user_name, user_coins):
    print_pause("\nWelcome to Guess The Number!")
    print_pause("\nHow to Play:")
    print_pause("A number between 1 to 20 (both inclusive) is selected.")
    print_pause("You have to guess the selected number in the least number of tries.")
    print_pause("After every wrong guess, "
                "you'll be provided a hint to guide you towards the number.", 0.75)
    print_pause("For every wrong guess you'll lose 25 coins each "
                "from the final reward of 500 coins.")
    print_pause("Well then, Good Luck!", 1.25)
    guess_play(user_name, user_coins)


def reward(user_name, user_coins, tries):
    reward_coins = 500 - (tries*25)
    user_coins += reward_coins
    print_pause(f"\nNumber of tries = {tries}")
    print_pause(f"You win {reward_coins} coins!")
    print_pause(f"\n{user_name} coins: \U0001FA99{user_coins}")
    return user_coins


def guess_play(user_name, user_coins):
    print_pause(f"Hello, {user_name}! I've picked a number between 1 to 20 (both inclusive).")
    print_pause("Can you guess what the number is? Give it a try!.")
    rndm = random.randint(1,20)
    tries = 1
    while True:
        user_guess = int(input())
        '''check user_guess'''
        if(rndm == user_guess):
            print("Good job,", user_name, "You guessed my number in", tries, "guesses!")
            user_coins = reward(user_name, user_coins, tries)
            break
        elif(user_guess < rndm):
            print("Your guess is too low.\nTry again.")
        elif(user_guess > rndm):
            print("Your guess is too high.\nTry again.")
        tries += 1


def play_again(user_name, user_coins):
    while True:
        choose = input("\nWould you like to play again (y/n)? ")
        if choose == 'y':
            guess_play(user_name, user_coins)
            break
        elif choose == 'n':
            print_pause("Thanks for playing!")
            break
        

guess_intro('ak', 500)
