import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def intro(party_list, lounge_list, drinks_list, items):
    print_pause("It's Saturday night!")
    print_pause("You are going out with a private party for "
                + random.choice(party_list) + "!")
    print_pause("You want to enjoy the vibes with your party in the VIP "
                "Lounge.")
    print_pause("You and your private party enter the "
                + random.choice(lounge_list) + " Lounge.")
    print_pause("The neon lights are shining, and the music is bumping!")
    print_pause("You see the VIP Lounge to your left, a bar in front of "
                "you, and the dance floor to your right.")
    area(party_list, lounge_list, drinks_list, items)


def play_again():
    print("Would you like to play again?")
    play_another = input(("Please say 'yes' or 'no'.\n").lower())
    if "no" in play_another:
        print_pause("Ok, get some rest. Goodbye!")
    elif "yes" in play_another:
        play_game()
    else:
        print("Sorry, please enter a valid response.")
        play_again()


def area(party_list, lounge_list, drinks_list, items):
    print("Which area would you like to visit? Please enter '1','2' or '3'.")
    response = input("Enter 1 for the VIP Lounge.\n" "Enter 2 for the bar.\n"
                     "Enter 3 for the dance floor.\n")
    if response == '1':
        vip(party_list, lounge_list, drinks_list, items)
    elif response == '2':
        bar(party_list, lounge_list, drinks_list, items)
    elif response == '3':
        dance_floor(party_list, lounge_list, drinks_list, items)
    else:
        print("Sorry, please enter a valid response.")
        area(party_list, lounge_list, drinks_list, items)


def vip(party_list, lounge_list, drinks_list, items):
    print_pause("You and your party approach the VIP Lounge.")
    print_pause("The 7-foot muscular bouncer standing at the entrance "
                "approaches you.")
    print_pause("He says 'You need a VIP wristband to enter!'")
    if "wristband" in items:
        print_pause("You show your wristband to the bouncer.")
        print_pause("The bouncer moves aside and lets you and your party "
                    "enter the VIP lounge!")
        print_pause("You dance the night away and enjoy the rest of the "
                    "night with your party.")
        print_pause("The next day, you wake up at 12 pm with a hoarse voice "
                    "and sore body. WHEW!")
        print_pause("You won Saturday Night!")
        play_again()
    else:
        print_pause("The bouncer notices you do not have a wristband...")
        print_pause("He grabs you by your shirt and throws you across the "
                    "lounge!")
        print_pause("Embarrassed, you get up determined to get a wristband "
                    "so you can enjoy your night with friends.")
        area(party_list, lounge_list, drinks_list, items)


def bar(party_list, lounge_list, drinks_list, items):
    print_pause("You and your friends approach the bar.")
    print_pause("The bartender, Mixa, greets you and asks what you'd like to "
                "drink.")
    print_pause("You order your favorite drink, "
                + random.choice(drinks_list) + ".")
    if "wristband" in items:
        print_pause("Mixa gives you your drink and moves on to the next "
                    "person.")
    else:
        print_pause("After giving you your drink, she tells you she has VIP "
                    "wristbands for sale.")
        print_pause("You purchase a VIP wristband. Now you're ready to party!")
        items.append("wristband")
    area(party_list, lounge_list, drinks_list, items)


def dance_floor(party_list, lounge_list, drinks_list, items):
    print_pause("You and your friends approach the dance floor.")
    print_pause("The DJ is playing all the trending TikTok songs.")
    print_pause("You get on the dance floor ready to dance!")
    print_pause("Someone is in the middle of the dance floor stealing all "
                "the shine...")
    if "wristband" in items:
        print_pause("Fortunately, you just learned the latest TikTok dances "
                    "so you're ready to battle!")
        print_pause("You battle the dancer in the middle of the dance floor "
                    "while the crowd cheers for you!")
        print_pause("The song goes off...and you WIN THE BATTLE!")
        print_pause("However, you are tired now and ready to sit down to "
                    "enjoy the rest of the night.")
        area(party_list, lounge_list, drinks_list, items)
    else:
        print_pause("You approch the middle of the dance floor to battle the "
                    "dancer.")
        print_pause("Unfortunately, their moves are too much for you to keep "
                    "up with.")
        print_pause("You slip and fall on the floor. Now you are hurt.")
        print_pause("Your friends have to carry you off the floor and take "
                    "you home.")
        print_pause("You ruined the night.")
        play_again()


def play_game():
    party_list = ["your coworker's birthday", "your best friend's bachelor "
                  "party", "New Year's"]
    lounge_list = ["Sip Sip Hooray", "Pour Decisions", "Neon Nights"]
    drinks_list = ["a Long Island Iced Tea", "an Old Fashioned", "a Daiquiri"]
    items = []
    intro(party_list, lounge_list, drinks_list, items)


play_game()
