import random
faces = ["heads","tails"]

def maingame():
    result = random.randint(0,1)
    if result == 0:
        print("Result is", faces[0], "!!!!!")
        again = input("Do you want to play again? Yes or No. >>")
        again = again.lower()
        if again == "yes":
            return whose_chance()
        elif again == "no":
            print("THANK YOU!!!")
        else:
            print("OOPS!Invalid input..")
    else:
        print("Result is", faces[1], "!!!!!")
        again = input("Do you want to play again? Yes or No. >>")
        again = again.lower()
        if again == "yes":
            return whose_chance()
        elif again == "no":
            print("THANK YOU!!!")
        else:
            print("OOPS!Invalid input..")

def player():
    inp = input("Which face you want to select? Heads or Tails.\n>>")
    inp = inp.lower()
    if inp == "heads":
        opponent = "tails"
        opponent = opponent.title()
        print("Computer >>",opponent,".")
        return maingame()
    elif inp == "tails":
        opponent = "heads"
        opponent = opponent.title()
        print("Computer >>",opponent,".")
        return maingame()
    else:
        print("Your input is invalid.Please double check it.")

def computer():
    comp = random.randint(0,1)
    if comp == 0:
        print("Computer selects",faces[0].title(),"!!!")
        print("You",faces[1].title(),"!!!")
        return maingame()
    else:
        print("Computer selects",faces[1].title(),"!!!")
        print("You",faces[0].title(),"!!!")
        return maingame()

def whose_chance():
    ask = input("Do you want to start? Yes or No.\n>>")
    ask = ask.lower()
    if ask == "yes":
        return print(player())
    elif ask == "no":
        return print(computer())
    else:
        print("OOPS!!Your input is Invalid.Please type again or you may close.")

whose_chance()




