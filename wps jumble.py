#ELI PRUSHANSKY 300919
#The function wpsJumble creates a list of names from the AP CS class, introduces the option to play for the user, gives the user a jumbled name, and allows the user to guess the original name.
#If correct, the user gets points and can play again. If incorrect, the user must restart. The user can quit at any time.
def wpsJumble():
    import random
    words = ("eli", "kathryn", "max", "spencer", "kurt", "frank", "prushansky", "marini", "huber", "paquette", "leinemann", "carter")
    print(
    """
               Welcome to WPS Jumble!

       Unscramble the letters to find the name of a student in the AP CS class.
    (Press the enter key at the prompt to quit.)
    """
    )
    play=input("Would you like to play? yes or no")
    while play=="yes":
        word = random.choice(words)
        correct = word
        jumble =""
        while word:
            position = random.randrange(len(word))
            jumble += word[position]
            word = word[:position] + word[(position + 1):]
        print("The name is:", jumble)
        points="+1"
        guess = input("\nWho is it: ")
        while guess != correct:
            print("Sorry, that's not it.")
            guess = input("Your guess: ")
        if guess == correct:
            print("You got it!\n")
            print("Your score: " + str(points))
            play=input("Would you like to play again? yes or no")
    print("Thanks for playing WPS Jumble.")
    input("\n\nPress the enter key to exit.")

wpsJumble()
