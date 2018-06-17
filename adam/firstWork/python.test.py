import random
exitChoice = "Nothing"
while exitChoice != "EXIT":
    
    print("You are in a dark castle in the dead of night")

    choseDoor = input("Before you are four doors. You must choose one of them. 1, 2, 3 or 4:  ")

    if choseDoor == "1":
        print("You die a slow death from being hit over the head with a club by an ogre ")
        print("GAME OVER")
        exit()
    elif choseDoor == "2":
        print("A dragon eats your brains with ketchup and hot sauce")
        print("You can guess what happens then")
        print("You Loooooooose")
        exit()
    elif choseDoor == "3":
        print("You find a sleeping ogre")
        print("You can 1) Try to steal his gold. 2) Just escape")
        choice1or2 = input("Choose option 1 or 2: ")

        if choice1or2 == "1":
            print("You get the gold and escape")
            exitChoice = input("Press return to play again, or type EXIT to leave: ")
            if exitChoice.lower() == "exit":
                exit()
        elif choice1or2 == "2":
            print("You die a gruesome death")
            exitChoice = input("Press return to play again, or type EXIT to leave: ")

            if exitChoice.lower() == "exit":
                exit()
            
    elif choseDoor == "4":
        print("You enter a room with a gigantic computer")
        print("It asks you to guess a number between 1 and 10")
        
        number = int(input("What do you choose: "))
        
        if number == random.randint(1,10):
            print("The computer lets you leave")
            print("YOU HAVE WON")
        else:
            print("The computer elecrocutes you")
            print("GAME OVER")
            if exitChoice.lower() == "exit":
                exit()
            exitChoice = input("Press return to play again, or type EXIT to leave: ")
