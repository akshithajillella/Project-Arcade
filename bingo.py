import time
import random
import re

final_coins = 0


def print_pause(message, sleep_time=0.5):
    print(message)
    time.sleep(sleep_time)


def bingo_intro(user_name, user_coins):
    print_pause("\nWelcome to Bingo!")
    print_pause("\nHow to Play:")
    print_pause("Pick 10 numbers from 1 to 100 (Numbers separated by ' ' or ',').")
    print_pause("    For Example: 1,2,3,4,5,6,7,8,9,10 or 1 2 3 4 5 6 7 8 9 10")
    print_pause("The computer displays 10 random numbers from 1 to 100.", 0.75)
    print_pause("You win coins if any of the numbers you picked "
                "match with the ones displayed.", 1)
    print_pause("You win 50 coins for each number match.", 1)
    print_pause("\nLet's get started!", 1.25)
    global final_coins
    final_coins = user_coins
    bingo_pick(user_name)
    return final_coins


def check_list(listToCheck):
    try:
        duplicate = len(listToCheck) == len(set(listToCheck))
        length = len(listToCheck) == 10
        not_in_range = list(x for x in listToCheck if int(x) < 1 or int(x) > 100)
    except(ValueError,UnboundLocalError) as error:
        print("Please pick integers only.")
        return False
    if duplicate and length and (len(not_in_range) == 0):
        return True
    else:
        if not duplicate:
            print("Please pick different numbers.")
        if not length:
            print("Please pick 10 numbers.")
        if len(not_in_range):
            print("Please pick numbers from 1 to 100.")
            print("Numbers not in range: ", not_in_range)
        return False


def bingo_pick(user_name):
    while True:
        input_str = input("\nPick 10 different numbers "
                               "from 1 to 100: ")
        user_pick = list(re.split(',| ', input_str))
        if check_list(user_pick):
            bingo_play(user_name,user_pick)
            break


def display_pick(comp_pick):
    print_pause("Here are the lucky numbers!\n")
    for i in comp_pick:
        print_pause(i, 1)


def random_list():
    list = []
    while len(list) != 10:
        r = str(random.randint(1, 100))
        if r not in list:
            list.append(r)
    return list


def check_match(user_pick, comp_pick):
    user_set = set(user_pick)
    comp_set = set(comp_pick)
    return list(user_set & comp_set)


def reward(user_name, match_list):
    match_num = len(match_list)
    reward_coins = match_num*50
    global final_coins
    final_coins += reward_coins
    print_pause(f"\nNumber of matches = {match_num}")
    print_pause(f"Matched numbers = {match_list}")
    print_pause(f"You win {reward_coins} coins!")
    print_pause(f"\n{user_name} coins: \U0001FA99{final_coins}")


def bingo_play(user_name,user_pick):
    print_pause(f"Your pick: {user_pick}")
    comp_pick = random_list()
    display_pick(comp_pick)
    match_list = check_match(user_pick, comp_pick)
    reward(user_name, match_list)
    play_again(user_name)


def play_again(user_name):
    while True:
        choose = input("\nWould you like to play again (y/n)? ")
        if choose == 'y':
            bingo_pick(user_name)
            break
        elif choose == 'n':
            print_pause("Thanks for playing!")
            break
