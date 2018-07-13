import random
import time


def repeat_fun(times, f):
    for i in range(times): f()


def start():
    greeting = input("Welcome to Hangman v0.1! Please select your difficulty level. Easy, Medium, or Hard.")
    i = ""
    if greeting == "Easy":
        animal_list = ("Lion", "Hyena", "Lemur", "Boar", "Elephant", "Giraffe", "Wildebeest", "Lemur", "Hippopotamus")
        ii = random.randint(0, len(animal_list)-1)
        i = animal_list[ii]
        print("_ " * len(animal_list[ii]))

    if greeting == "Medium":
        weather_list = ("Lightning", "Thunder", "Hail", "Sunny", "Cumulus", "Playwright", "Accommodate", "Receive")
        ii = random.randint(0, len(weather_list)-1)
        i = weather_list[ii]

        print("- " * len(weather_list[ii]))
    if greeting == "Hard":
        space_list = ("Planetary Nebula", "Albedo", "Antimatter", "Gamma Ray", "Serendipitous", "Geodesic", "Hydrost"
                                                                                                    "atic Equilibrium")
        ii = random.randint(0, len(space_list)-1)
        i = space_list[ii]
        print("- " * len(space_list[ii]))

    time.sleep(3)
    print("   ______")
    print("   |    |")
    print("        |")
    print("        |")
    print("        |")
    print("        |")
    print("       ___")
    guesser(i)
    attempts(a)


def guesser(i):
    g = 0
    gg = []
    a = i
    while g < len(a):
        gg.append("_")
        g += 1
    while True:
        a = i
        gg = []
        g = 0
        print(i)
        letter = input("Input a letter: ")
        xx = 0
        correct = False
        while xx < len(a):
            print(xx)
            if letter == a[xx]:
                gg[xx] = letter
                correct = True
            xx += 1
        if correct:
            print(gg)


def attempts(a):
    lives = 7
    while lives > len(a):
        if correct == True:
            print(str.replace(_, letter))
            print(gg)
            while tries < len(word):
                if letter in word:
                    lives += 1

                if letter not in word:
                    lives -= 1
                    if lives == 6:
                        image1()
                    elif lives == 5:
                        image2()
                    elif lives == 4:
                        image3()
                    elif lives == 3:
                        image4()
                    elif lives == 2:
                        image5()
                    elif lives == 1:
                        image6()
                    elif lives == 0:
                        loss()


def image1():
    print("   ______")
    print("  _|     |")
    print(" {..}    |")
    print("         |")
    print("         |")
    print("         |")
    print("        ___")
    guesser(i)
    attempts(a)


def image2():
    print("   ______")
    print("  _|     |")
    print(" {..}    |")
    print("*-|      |")
    print("         |")
    print("         |")
    print("        ___")
    guesser(i)
    attempts(a)


def image3():
    print("   ______")
    print("  _|     |")
    print(" {..}    |")
    print("*-|-*    |")
    print("         |")
    print("         |")
    print("        ___")
    guesser(i)
    attempts(a)


def image4():
    print("   ______")
    print("  _|     |")
    print(" {..}    |")
    print("*-|-*    |")
    print("  |      |")
    print("         |")
    print("        ___")
    guesser(i)
    attempts(a)


def image5():
    print("   ______")
    print("  _|     |")
    print(" {..}    |")
    print("*-|-*    |")
    print("  |      |")
    print("_/       |")
    print("        ___")
    guesser(i)
    attempts(a)


def image6():
    print("   ______")
    print("  _|     |")
    print(" {..}    |")
    print("*-|-*    |")
    print("  |      |")
    print("_/ \_    |")
    print("        ___")
    guesser(i)
    attempts(a)


def loss():
    print("    ____")
    print("   _|    |")
    print("  {..}   |")
    print(" *-|-*   |")
    print("   |     |")
    print(" _/ \_   | ")
    print("        ---")
    print("You have lost. Restarting now.")
    repeat_fun(1, start())


start()

