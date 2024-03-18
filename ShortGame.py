# Adventure in Whereverland

# game introduction
def start_game():
    print("-" * 78)
    print("This a short game for the author to practice Python coding. You will enter the remarkable and  "
          "fantastical yet utterly mundane world of Whereverland, where your choices will count for "
          "everything/something/nothing!")
    print("-" * 78)
    print("\n")
    print("Let's begin...\n")
    print("Maybe it's like an isekai or something. You died in a freak pigeon attack and then woke up in another world."
          " You find yourself in a clearing in a dark forest. It looks like whatever brought you here obliterated "
          "everything within a ten foot circular diameter around you.\n")


# first scenario
def first_scenario():
    print(
        "You could try walking in one direction until you find someone to help you. Alternatively, you could "
        "investigate the local area for any resources that might help you survive the night. What will you do?\n")
    print("1. Attempt to walk out of the forest.")
    print("2. Forage the immediate area.")

    # player's choice
    choice = input("What do you choose? (1/2): ")

    # Based on the choice, go to the next part of the story
    if choice == '1':
        second_scenario()
    elif choice == '2':
        third_scenario()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        first_scenario()  # Restart this scenario if the input is invalid


#  branching second scenario
def second_scenario():
    print("\n")
    print(
        "You walk for hours in the same direction. At least, you hope you do as you have no compass. Eventually you "
        "come across a still pool. You are thirsty now but you don't know if the water is clean. Will you drink it?\n")
    print("1. Drink.")
    print("2. Abstain.")

    # player's choice
    choice = input("What do you choose? (1/2): ")

    # Based on the choice, go to the next part of the story
    if choice == '1':
        ending_one()
    elif choice == '2':
        ending_two()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        first_scenario()  # Restart this scenario if the input is invalid


# branching third scenario
def third_scenario():
    print("\n")
    print(
        "Foraging for supplies seems sensible at first glance. Unfortunately, it turns out that in your past life you "
        "were an urbanite with no practical skills for living off the land. As night falls it becomes very cold. "
        "Now you're hungry, thirsty and shivering in the middle of the night. There's some mushrooms you picked "
        "but you have no idea if they are safe to eat. Will you dare eat them for some much-needed energy?\n")
    print("1. Eat the mushrooms.")
    print("2. Ignore them and try to last the night by curling up into a ball.")

    # player's choice
    choice = input("What do you choose? (1/2): ")

    # Based on the choice, go to the next part of the story
    if choice == '1':
        ending_three()
    elif choice == '2':
        ending_four()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        first_scenario()  # Restart this scenario if the input is invalid


# first ending
def ending_one():
    print(
        "You cup water from the pool in your hands and drink. It brings much needed refreshment. However, a few hours "
        "later you start to feel tummy ache. Despite many hours of walking it seems like there's no end to this forest "
        "this day and as night falls, you find the temperature drops dramatically. Hungry and thirsty, with no "
        "protection from the elements, you die in agony from exposure.\n")
    print("+" * 78)
    print(   "Would you like to try again from the beginning? "
        "You will be reborn and get to try again.")
    print("+" * 78)
    print("1. Restart")
    print("2. End")

    # player's choice
    choice = input("What do you choose? (1/2): ")

    # Based on the choice, go to the next part of the story
    if choice == '1':
        restart()
    elif choice == '2':
        print("+" * 78 + "\n")
        print("So ends your adventure in Whereverland.\n")
        print("+" * 78 + "\n")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        first_scenario()  # Restart this scenario if the input is invalid


# second ending
def ending_two():
    print(
        "It seems like a wise choice to avoid drinking from a stagnant pool. However, you become dehydrated after "
        "walking for several hours. Despite many hours of walking it seems like there's no end to this forest this "
        "day and as night falls, you find the temperature drops dramatically. Hungry and thirsty, with no protection "
        "from the elements, you die of exposure.\n")
    print("+" * 78)
    print(   "Would you like to try again from the beginning? "
        "You will be reborn and get to try again.")
    print("+" * 78)
    print("1. Restart")
    print("2. End")

    # player's choice
    choice = input("What do you choose? (1/2): ")

    # Based on the choice, go to the next part of the story
    if choice == '1':
        restart()
    elif choice == '2':
        print("+" * 78 + "\n")
        print("So ends your adventure in Whereverland.\n")
        print("+" * 78 + "\n")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        first_scenario()  # Restart this scenario if the input is invalid


# third ending
def ending_three():
    print(
        "The raw mushrooms taste okay. However, a few hours later you start to feel tummy ache, which only gets worse "
        "over time. The night becomes freezing cold and you die in agony from exposure.\n")
    print("+" * 78)
    print(   "Would you like to try again from the beginning? "
        "You will be reborn and get to try again.")
    print("+" * 78)
    print("1. Restart")
    print("2. End")

    # player's choice
    choice = input("What do you choose? (1/2): ")

    # Based on the choice, go to the next part of the story
    if choice == '1':
        restart()
        print("+" * 78 + "\n")
        print("So ends your adventure in Whereverland.")
        print("+" * 78 + "\n")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        first_scenario()  # Restart this scenario if the input is invalid


# fourth ending
def ending_four():
    print(
        "It's impossible to know if the mushrooms are safe to consume, better not to risk it. The night becomes "
        "freezing cold. Hungry and thirsty, with no protection from the elements, you die of exposure.")
    print("+" * 78)
    print(   "Would you like to try again from the beginning?"
        "You will be reborn and get to try again.\n")
    print("+" * 78)
    print("1. Restart")
    print("2. End")

    # player's choice
    choice = input("What do you choose? (1/2): ")

    # Based on the choice, go to the next part of the story
    if choice == '1':
        restart()
    elif choice == '2':
        print("+" * 78 + "\n")
        print("So ends your adventure in Whereverland.\n")
        print("+" * 78 + "\n")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        first_scenario()  # Restart this scenario if the input is invalid


# restart point
def restart():
    print("\n")
    print("You find yourself in a clearing in a dark forest. It looks like whatever brought you here obliterated "
          "everything within a ten foot circular diameter around you. It feels familiar for some reason.")
    first_scenario()  # Move to the first scenario

# Main function to start the game
def main():
    start_game()
    first_scenario()


# This is the standard boilerplate that calls the main() function.
if __name__ == "__main__":
    main()