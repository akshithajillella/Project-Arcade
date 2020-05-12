import random

score = 500


def intro():
    print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
    play()
  
def play():
    global score
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n") 
      
    choice = int(input("User turn: ")) 
      
    
    while choice > 3 or choice < 1: 
        choice = int(input("enter valid input: ")) 
          
    if choice == 1: 
        choice_name = 'Rock'
    elif choice == 2: 
        choice_name = 'paper'
    else: 
        choice_name = 'scissor'
          
# print user choice  
    print("user choice is: " + choice_name) 
    print("\nNow its computer turn.......") 
    comp_choice = random.randint(1, 3) 

    if comp_choice == 1: 
        comp_choice_name = 'Rock'
    elif comp_choice == 2: 
        comp_choice_name = 'paper'
    else: 
        comp_choice_name = 'scissor'
          
    print("Computer choice is: " + comp_choice_name) 
  
    print(choice_name + " V/s " + comp_choice_name) 
  
   
    if((choice == 1 and comp_choice == 2) or
        (choice == 2 and comp_choice ==1 )): 
        print("paper wins => ", end = "") 
        result = "paper"
          
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)): 
        print("Rock wins =>", end = "") 
        result = "Rock"
    else: 
        print("scissor wins =>", end = "") 
        result = "scissor"
  
    if result == choice_name: 
        print("<== User wins ==>")
        print("U scored 50 coins")
        score = score+50
    else: 
        print("<== Computer wins ==>")
        print("U lost 50 coins")
        score = score-50
    print(f"Your current balance is {score}")
    play_again()
    return score


def play_again():
    while True:
        begin = input("Would you like to play again?(y/n)")
        if begin == "y":
            play()
        elif begin == "n":
            print("Thanks for playing.")
            break
