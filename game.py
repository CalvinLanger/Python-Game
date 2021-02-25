#Made by Calvin Langer

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
    print("The barrel rolls aside and you find a secret tunnel. What do you do?")

    secret_tunnel = str(input())
    if secret_tunnel == "Enter tunnel":
        print("You start to escape but your friend is too weak to go with you")
        print("They hand you a note. What do you do?")
    
    elif secret_tunnel == "Read them":
        print("It is too dark to read the note. What do you do?")

    elif secret_tunnel == "Light a match":
        print("The note says: Don't "/"leave me here")
        print("Dou you leave your friend or stay?")
        
        stay = str(input())
        if stay == "Stay":
            print("That's over... You prove it, your heart is big...")
    

        go_next = str(input())
        if go_next == "Leave":
            print("You crawl through the tunnel and the tunnel leads you to a beach")
            print("What do you do?")

            look = str(input())
            if look == "Look":
                print("In the water you see a boat")
                print("What do you do?")

                boat = str(input())
                if boat == "Get on the boat":
                    print("Congratulations, you're heading to a new world.")
                    print("Do you want to play again?")
                    
            else:
                print("You die...")


        else:
            print("You die...")
    else:
        print("You die...")

else:
    print("You die...")



