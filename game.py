#Made by Calvin Langer

print("Welcome to Python Game!")

name = input("Write your name: ")
age = int(input("Write your age: "))


if age >= 18:
    print("You have good age to play!")

want_to_play = str(input("Do you want to play? "))

if want_to_play == ["Yes", "yes", "Y", "y"]:
    print("Let's play!")
elif want_to_play == ["No", "no", "N", "n"]:
    print("Meybe you wanna be play another time...")

elif age < 18:
    print("You are to young to play traveler!")






