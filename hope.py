import random


def repeat_fun(times, f):
    for i in range(times): f()


def image1():
    print("   ______")
    print("  _|     |")
    print(" {..}    |")
    print("         |")
    print("         |")
    print("         |")
    print("        ___")



def image2():
    print("   ______")
    print("  _|     |")
    print(" {..}    |")
    print("*-|      |")
    print("         |")
    print("         |")
    print("        ___")


def image3():
    print("   ______")
    print("  _|     |")
    print(" {..}    |")
    print("*-|-*    |")
    print("         |")
    print("         |")
    print("        ___")



def image4():
    print("   ______")
    print("  _|     |")
    print(" {..}    |")
    print("*-|-*    |")
    print("  |      |")
    print("         |")
    print("        ___")


def image5():
    print("   ______")
    print("  _|     |")
    print(" {..}    |")
    print("*-|-*    |")
    print("  |      |")
    print("_/       |")
    print("        ___")


def image6():
    print("   ______")
    print("  _|     |")
    print(" {..}    |")
    print("*-|-*    |")
    print("  |      |")
    print("_/ \_    |")
    print("        ___")


def loss():
    print("    ____")
    print("   _|    |")
    print("  {..}   |")
    print(" *-|-*   |")
    print("   |     |")
    print(" _/ \_   | ")
    print("        ---")
    tap = input("You have lost. Would you like to restart?")
    if tap == "Yes":
        repeat_fun(1, start())


def start():
    print("   ______")
    print("   |    |")
    print("        |")
    print("        |")
    print("        |")
    print("        |")
    print("       ___")
    #word = easy[random_number]
    funct = [image1, image2, image3, image4, image5, image6, loss]
    lives = 0
    correct_letters_total = 0
    x = 0
    blank = []
    greeting = input("Welcome to Hangman v0.1! Please select your difficulty level. Easy, Medium, or Hard.")
    i = ""
    if greeting == "Easy":
        animal_list = ("Lion", "Hyena", "Lemur", "Boar", "Elephant", "Giraffe", "Wildebeest", "Lemur", "Hippopotamus")
        random_number = random.randint(0, len(animal_list)-1)
        i = animal_list[random_number]
        word = animal_list[random_number]
        print("_ " * len(animal_list[random_number]))
        while (x < len(word)):
            blank.append('_')
            x += 1
        while (lives < len(funct)):
            guessedletter = input("Pick a letter: ")
            x = 0
            in_word = False
            while (x < len(word)):
                if (guessedletter == word[x]):
                    in_word = True
                    blank[x] = guessedletter
                    break
                x += 1
            if (in_word):
                print("Correct!")
                correct_letters_total += 1
                print(blank)
            else:
                print("Incorrect!")
                print(funct[lives]())
                lives += 1
            if (correct_letters_total == len(word)):
                print("You win!")
                break
            if (lives == len(funct)):
                print("You lose!\n The correct answer is " + word)


    if greeting == "Medium":
        weather_list = ("Lightning", "Thunder", "Hail", "Sunny", "Cumulus", "Playwright", "Accommodate", "Receive")
        random_number = random.randint(0, len(weather_list)-1)
        i = weather_list[random_number]
        word = i

        print("- " * len(weather_list[random_number]))
        while (x < len(word)):
            blank.append('_')
            x += 1
        while (lives < len(funct)):
            guessedletter = input("Pick a letter ")
            x = 0
            in_word = False
            while (x < len(word)):
                if (guessedletter == word[x]):
                    in_word = True
                    blank[x] = guessedletter
                    break
                x += 1
            if (in_word):
                print("Correct!")
                correct_letters_total += 1
                print(blank)
            else:
                print("Incorrect!")
                print(funct[lives]())
                lives += 1
            if (correct_letters_total == len(word)):
                print("You win!")
                break
            if (lives == len(funct)):
                print("You lose!\n The correct answer is " + word)

    if greeting == "Hard":
        space_list = ("Planetary Nebula", "Albedo", "Antimatter", "Gamma Ray", "Serendipitous", "Geodesic", "Hydrost"
                                                                                                    "atic Equilibrium")
        random_number = random.randint(0, len(space_list)-1)
        i = space_list[random_number]
        word = space_list[random_number]
        print("- " * len(space_list[random_number]))
        while (x < len(word)):
            blank.append('_')
            x += 1
        while (lives < len(funct)):
            guessedletter = input("Pick a letter: ")
            x = 0
            in_word = False
            while (x < len(word)):
                if (guessedletter == word[x]):
                    in_word = True
                    blank[x] = guessedletter
                    break
                x += 1
            if (in_word):
                print("Correct!")
                correct_letters_total += 1
                print(blank)
            else:
                print("Incorrect!")
                print(funct[lives]())
                lives += 1
            if (correct_letters_total == len(word)):
                print("You win!")
                break
            if (lives == len(funct)):
                print("You lose!\n The correct answer is " + word)
    print("   ______")
    print("   |    |")
    print("        |")
    print("        |")
    print("        |")
    print("        |")
    print("       ___")


start()