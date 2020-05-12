from random import randint
from time import sleep


def print_pause(message, sleep_time=0.75):
    print(message)
    sleep(sleep_time)


def dice_roll_per(user_name, user_coins):
    print_pause(f"Your current balance is {user_coins}")
    play_again = input("Do you want to play again (y/n)?")
    if play_again == "y":
        dice_roll(user_name, user_coins)
    else:
        print("Thanks for playing")
        exit


def dice_roll_intro(user_name, user_coins):
    print_pause("\nWelcome to 7 UP and DOWN game")
    print_pause(f"\nDear {user_name}, you are having {user_coins} coins")
    print_pause("\nIn this game two dice are rolled and based on their outcome you will be rewarded")
    print_pause("\nYou will be given chance to bet based on the outcome")
    print_pause("\nYou can choose on the range of the number then you will be rewarded twice or thrice of your bet coins respectively")
    print_pause("\n 1) 2 to 6 then X2 \n 2) 7 then X3 \n 3) 8 to 12 then X2 \n")
    dice_roll(user_name, user_coins)


def dice_roll(user_name, user_coins):
    choice = int(input("\nEnter your choice : "))
    bet_amount = int(input("\nEnter your bet amount : "))
    if bet_amount < 100 :
        print("\nMinimum bet amount is 100 ")
        bet_amount = int(input("\nEnter bet amount : "))
    elif bet_amount > user_coins:
        print("\nInsufficient coins")
        bet_amount = int(input("\nEnter bet amount : "))
    user_coins = user_coins - bet_amount
    mini = 2
    maxi = 12
    check = randint(mini,maxi)
    print_pause(f"\nSum of numbers appeared when dice are rolled is {check}\n")
    if choice == 1:
        if 2 <= check and check <= 6:
            user_coins += bet_amount*2
            print_pause("\n**************YOU WIN************\n")
            dice_roll_per(user_name, user_coins)
        else:
            print_pause("\n**************YOU LOSE**************\n")
            dice_roll_per(user_name, user_coins)
    elif choice == 2:
        if check==7:
             user_coins += bet_amount*3
             print_pause("\n**************YOU WIN************\n")
             dice_roll_per(user_name, user_coins)
        else:
            print_pause("\n**************YOU LOSE**************\n")
            dice_roll_per(user_name, user_coins)
    else:
        if 8 <= check and check <= 12:
             user_coins += bet_amount*3
             print_pause("\n**************YOU WIN************\n")
             dice_roll_per(user_name, user_coins)
        else:
            print_pause("\n**************YOU LOSE**************\n")
            dice_roll_per(user_name, user_coins)


#dice_roll_intro("priyanka",500)
#dice_roll("priyanka",500)
