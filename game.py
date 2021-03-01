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


barrel = str(input("You see the barrel. What do you do? \nMove the barrel / Nothing \n"))

if barrel == "Move the barrel":
    
    secret_tunnel = str(input("The barrel rolls aside and you find a secret tunnel. What do you do? \nEnter tunnel / Nothing \n"))
    if secret_tunnel == "Enter tunnel":
        print("You start to escape but your friend is too weak to go with you")
        
        hand_note = str(input("They hand you a note. What do you do? \nLeave / Read them \n"))
        if hand_note == "Leave":
            print("You crawl through the tunnel and the tunnel leads you to a beach")

            leave = str(input("What do you do? \nLook / Nothing \n"))
            if leave == "Look":
                print("In the water you see a boat")

                boat = str(input("What do you do? \nGet on the boat / Nothing \n"))
                if boat == "Get on the boat":
                    print("Congratulations, you're heading to a new world.")
                    print("Do you want to play again?")

                    #Start new game
                    #Or stop them
                    #Write function or loop
                    to_the_beggining = str(input("Yes / No \n"))
                    if to_the_beggining == "Yes":
                        print("Start new game!")
                    elif to_the_beggining == "No":
                        print("Stop Game!")
                else:
                    print("You died on the beach...")

        elif hand_note == "Read them":
            print("It is too dark to read the note.")

            light = str(input("What do you do? \nLight a match / Leave \n"))
            if light == "Light a match":
                print("The note says: Don't leave me here")   

                stay = str(input("Do you leave your friend or stay? \nStay / Leave \n"))
                if stay == "Stay":
                    print("That's over... You prove it, your heart is big...")  
                elif light == "Leave":
                    leave #back to the hand note with egual "Leave"
            elif light == "Leave": 
                leave #back to the hand note with egual "Leave"
    else:
        print("You died...")#If you don't enter tunnel
else:
    print("You died...") #If you don't "Move the barrel"



