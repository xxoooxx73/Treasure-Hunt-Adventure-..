def start_the_game():
    print("Welcome to the Treasure Hunt Adventure!")
    answer = input("Do you want to explore a cave or jungle ? [cave/jungle]")
    if answer == "cave":
        cave()
    elif answer == "jungle":
        jungle()
    else:
        print("That's not a valid answer")
def cave():
    print("You go into the cave and see a sleeping bear . 🐻💤")
    answer = input("Do you want to fight or run ? [fight/run]")
    if answer == "fight":
        print("Bear is really strong! You lose!😈")
        answer = input("try again ? [yes/no]")
        if answer == "yes":
            start_the_game()
        else:
            pass
    elif answer == "run":
        print("You've returned to the starting point.")
        answer = input("Do you want to go to the jungle? [yes/no]")
        if answer == "yes":
            jungle()
        else:
            pass
    else:
        print("That's not a valid answer")

def jungle():
    print("You go into the jungle . ")
    answer = input(" Do you want to move forward ? [yes/no]")
    if answer == "yes":
        Next_stage()
    elif answer == "no" :
        print("You are still in the jungle . ")
    else:
        print("That's not a valid answer")

def Next_stage():
    print("You moved forward and found a hole .🕳️")
    answer = input("Do you want to explore what's inside ? [yes/no]")
    if answer == "yes":
        print("You found the treasure! you win ! 😒🎉💰")
        answer = input("Play again ? [yes/no]")
        if answer == "yes":
          start_the_game()
        else:
           print("المركب ال تودي!")
    else:
       print("أُمال أنت عايز إيه ؟!🤬 ")

start_the_game()





