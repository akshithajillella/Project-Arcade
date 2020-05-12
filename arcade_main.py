import time
import bingo
import guess_the_number
import dice_roll
import rock_paper_scissors

user_name = ''
user_coins = 500


def print_pause(message, sleep_time=0.5):
    print(message)
    time.sleep(sleep_time)


def intro():
    print_pause("Welcome to Internal 2 Arcade!")
    print_pause("We hope you have a great time.")
    print_pause("Shall we get started?")
    user_name = str(input("Enter username: "))
    print_pause(f"\nWelcome {user_name}!\nYour coins: \U0001FA99{user_coins}")
    choose_act(user_name, user_coins)


def choose_act(user_name, user_coins):
    while True:
        print_pause("\nWhat would you like to do?\n"
                    "1. Check out the games!\U0001F3AE\n"
                    "2. Know your balance\U0001F4B0\n"
                    "3. Quit\U0001F622")
        choose = input("Your choice? ")
        if choose == '1':
            games_menu(user_name, user_coins)
            break
        elif choose == '2':
            check_coins(user_name, user_coins)
            break
        elif choose == '3':
            print_pause(f"\nThanks for visiting us, {user_name}!")
            print_pause("See you again!!")
            break


def check_coins(user_name, user_coins):
    print(f"\nUsername: {user_name}")
    print(f"Coins: \U0001FA99{user_coins}")
    choose_act(user_name, user_coins)


def games_menu(user_name, user_coins):
    print_pause("\nGames:\n"
                "1. Rock paper scissors\n"
                "2. Guess the Number!\n"
                "3. Dice Rolling\U0001F3B2\n"
                "4. Bingo!")
    while True:
        choose_game = input("\nWhich game would you like to play?\n")
        if choose_game == '1':
            user_coins = rock_paper_scissors.play()
            break
        elif choose_game == '2':
            user_coins = guess_the_number.guess_intro(user_name, user_coins)
            break
        elif choose_game == '3':
            user_coins = dice_roll.dice_roll_intro(user_name, user_coins)
            break
        elif choose_game == '4':
            user_coins = bingo.bingo_intro(user_name, user_coins)
            break
    choose_act(user_name, user_coins)


intro()
