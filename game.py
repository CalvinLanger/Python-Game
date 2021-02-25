#Made by Calvin Langer


#Intro to the game
white_rose_words = [
"White Rose speaking...",
"I have learned to listen when time speaks",
"Our paths were too precisley linked to this moment",
"For therer not be a reason",
"This is why",
"You get to decide..."
]

for x in white_rose_words:
    print(x, "\n")

print("You're trapped in a dungeon with your friend")


barrel = str(input("You see the barrel. What do you do? \n"))

if barrel == "Move the barrel":
    
    secret_tunnel = str(input("The barrel rolls aside and you find a secret tunnel. What do you do? \n"))
    if secret_tunnel == "Enter tunnel":
        print("You start to escape but your friend is too weak to go with you")
        
        hand_note = str(input("They hand you a note. What do you do? \n"))
        if hand_note == "Leave":
            print("You crawl through the tunnel and the tunnel leads you to a beach")

            look = str(input("What do you do? \n"))
            if look == "Look":
                print("In the water you see a boat")

                boat = str(input("What do you do? \n"))
                if boat == "Get on the boat":
                    print("Congratulations, you're heading to a new world.")
                    print("Do you want to play again?") #Add function to start on beggining!
                else:
                print("You die on the beach...")
    
        elif secret_tunnel == "Read them":
            print("It is too dark to read the note. What do you do? \n") #Add function back to the hand_note statment

        elif secret_tunnel == "Light a match":
            print("The note says: Don't "/"leave me here")
            
            stay = str(input("Dou you leave your friend or stay?"))
            if stay == "Stay":
                print("That's over... You prove it, your heart is big...")

        else:
            print("You die...")
    else:
        print("You die...")
else:
    print("You die...")



