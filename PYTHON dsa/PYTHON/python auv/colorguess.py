import random
colours = ["red", "orange", "yellow", "green", "blue"]
chosen_colour = random.choice(colours)
witty_answers = {
    "red": "You are probably seeing RED right now.",
    "orange": "Don't let this ORANGE you out.",
    "yellow": "Don't be YELLOW, try again.",
    "green": "I bet you are GREEN with envy.",
    "blue": "You are probably feeling BLUE right now."
}
guesses = 0
while True:
    print("Pick a colour from these options: " + ", ".join(colours))
    user_colour = input("Enter your colour: ").lower()
    guesses += 1
    if user_colour == chosen_colour:
        print("Well done! You guessed it correctly in " + str(guesses) + " guesses.")
        break
    else:
        print(witty_answers[chosen_colour])
        print("Guess again.")
